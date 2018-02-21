extern crate gnuplot;
extern crate image;

use std::fs::File;
use std::f64;


use gnuplot::{Figure, Color};


fn main() {
    let imgx = 800;
    let imgy = 800;

    let scalex = 2.0/imgx as f64;
    let scaley = 16.0/imgy as f64;

    let mut imgbuf = image::ImageBuffer::new(imgx,imgy);
    
    
    let init = (3.0,0.0);
    let loop_count = 100000 as usize ;
    let h = 2.0*std::f64::consts::PI / 100.0;
    //let h = 0.01;
    let mut q_res = Vec::new(); 
    let mut p_res = Vec::new(); 
    func_loop(init, loop_count, h,&mut q_res,&mut p_res);

    //let mut fg = Figure::new();
    //fg.axes2d()
    //.points(&q_res, &p_res, &[Color("blue")]);

    //fg.set_terminal("png", "test.png");
    //fg.show();
    let mut calc_buf = vec![vec![0 as i32; imgy as usize]; imgx as usize];

    for i in 0..loop_count{
        let x = ((q_res[i]-2.0)/scalex) as i32;
        let y = ((p_res[i]+8.0)/scaley) as i32;
        if 0<=x &&x+2 <imgx as i32 && 0<=y && y+2<imgy as i32 {
            calc_buf[0+x as usize][y as usize] += 1;
            calc_buf[1+x as usize][y as usize] += 2;
            calc_buf[2+x as usize][y as usize] += 1;
            calc_buf[0+x as usize][1+y as usize] += 2;
            calc_buf[1+x as usize][1+y as usize] += 3;
            calc_buf[2+x as usize][1+y as usize] += 2;
            calc_buf[0+x as usize][2+y as usize] += 1;
            calc_buf[1+x as usize][2+y as usize] += 2;
            calc_buf[2+x as usize][2+y as usize] += 1;
        }
    }
    let mut max = 0;
    for v in &calc_buf[..]{
        for x in v{
            max = std::cmp::max(max, *x);
        }
    }
    println!("{}",max);
    for (x,y,pixel) in imgbuf.enumerate_pixels_mut(){
        let normal = std::cmp::min(255,(1<<11) * calc_buf[x as usize][y as usize] /max) ; 
        
        *pixel = image::LumaA([255 - normal as u8,255]) ;
        if x==0 && y==0 {
            *pixel = image::LumaA([255 - normal as u8,0]) ;
        }
    }

    let fout = &mut File::create("testimg.png").unwrap();

    image::ImageLumaA8(imgbuf).save(fout, image::PNG).unwrap();
}
fn func_loop(init:(f64,f64),lp:usize,h:f64,q_res: &mut std::vec::Vec<f64> ,p_res :&mut  std::vec::Vec<f64>){
    let (mut q,mut p) = init;
    q_res.reserve(lp);
    p_res.reserve(lp);
    for i in 0..lp{
        q_res.push(q) ;
        p_res.push(p) ;
        for j in 0..100{
            let t = (100*i + j) as f64 * h;
            runge_kutta_loop(&mut q,&mut p, h, t);
        }
    }
}

fn del_h(q:f64,p:f64,t:f64)->(f64,f64){
    (p,-0.1*p - q*q*q + 12.0 * t.cos())
}
fn runge_kutta_loop(q:&mut f64, p:&mut f64 ,h: f64,t: f64){
    let (dq1,dp1) = del_h(*q, *p, t);
    let (dq2,dp2) = del_h(*q + h*dq1/2.0, *p+h*dp1/2.0, t + h/2.0);
    let (dq3,dp3) = del_h(*q + h*dq2/2.0, *p+h*dp2/2.0, t + h/2.0);
    let (dq4,dp4) = del_h(*q + h*dq3, *p+h*dp3, t + h);
    
    *q += h*(dq1/6.0 + dq2/3.0 + dq3/3.0 + dq4/6.0);
    *p += h*(dp1/6.0 + dp2/3.0 + dp3/3.0 + dp4/6.0);
}

