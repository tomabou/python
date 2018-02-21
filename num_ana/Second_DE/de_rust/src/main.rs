extern crate gnuplot;
extern crate image;

use gnuplot::{Figure, Color};

fn main() {
    println!("Hello, world!");
    let init = (1.0,0.0);
    let time = 1000.0;
    let h = 0.01;
    let mut q_res = Vec::new(); 
    let mut p_res = Vec::new(); 
    func_loop(init, time, h,&mut q_res,&mut p_res);
    let mut fg = Figure::new();
    fg.axes2d()
    .points(q_res,p_res,&[Color("blue")]);

    fg.set_terminal("png", "test.png");
    fg.show();
}
fn func_loop(init:(f64,f64),time:f64,h:f64,q_res: &mut std::vec::Vec<f64> ,p_res :&mut  std::vec::Vec<f64>){
    let (mut q,mut p) = init;
    let lp = (time / (h* 1000.0)) as usize;
    q_res.reserve(lp);
    p_res.reserve(lp);
    for i in 0..lp{
        q_res.push(q) ;
        p_res.push(p) ;
        for j in 0..1000{
            let t = (1000*i + j) as f64 * time;
            runge_kutta_loop(&mut q,&mut p, h, t);
            
        }
    }
}

fn del_h(q:f64,p:f64,t:f64)->(f64,f64){
    (p,-q)
}
fn runge_kutta_loop(q:&mut f64, p:&mut f64 ,h: f64,t: f64){
    let (dq1,dp1) = del_h(*q, *p, t);
    let (dq2,dp2) = del_h(*q + h*dq1/2.0, *p+h*dp1/2.0, t + h/2.0);
    let (dq3,dp3) = del_h(*q + h*dq2/2.0, *p+h*dp2/2.0, t + h/2.0);
    let (dq4,dp4) = del_h(*q + h*dq3, *p+h*dp3, t + h);
    
    *q += h*(dq1/6.0 + dq2/3.0 + dq3/3.0 + dq4/6.0);
    *p += h*(dp1/6.0 + dp2/3.0 + dp3/3.0 + dp4/6.0);
}

