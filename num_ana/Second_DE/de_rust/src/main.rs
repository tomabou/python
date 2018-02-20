extern crate gnuplot;


use gnuplot::{Figure, Color};

fn main() {
    println!("Hello, world!");
    let (a,b) = runge_kutta_loop(2.0,3.0,0.1,100);
    println!("{},{}",a,b);
    let mut fg = Figure::new();
    fg.axes2d()
    .lines(&[1, 2, 3], &[4, 5, 6], &[Color("blue")])
    .lines(&[1, 2, 3], &[7, 6, 5], &[Color("red")]);

    fg.set_terminal("png", "test.png");
    fg.show();
}

fn del_h(q:f64,p:f64,t:f64)->(f64,f64){
    (p,-q)

}
fn runge_kutta_loop(q: f64, p: f64 ,h: f64,counter: i64)->(f64,f64){
    let t = h* counter as f64;
    let (dq1,dp1) = del_h(q, p, t);
    let (dq2,dp2) = del_h(q + dq1/2.0, p+dp1/2.0, t + h/2.0);
    let (dq3,dp3) = del_h(q + dq2/2.0, p+dp2/2.0, t + h/2.0);
    let (dq4,dp4) = del_h(q + dq3, p+dp3, t + h);
    
    (q + h*(dq1/6.0 + dq2/3.0 + dq3/3.0 + dq4/6.0)
    ,p + h*(dp1/6.0 + dp2/3.0 + dp3/3.0 + dp4/6.0))
}

