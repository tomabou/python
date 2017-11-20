use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::open("../BCCWJ_frequencylist_suw_ver1_0.tsv").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents);
    println!("Hello, world!");
    let s = "hello".to_string();
    println!("{}", s);
    let t = Test::new(3,2);
    t.func();
    
}

#[derive(Debug)]
struct Test {
    v1: i32,
    v2: i32,
}
impl Test {
    fn new(x: i32,y: i32)->Test{
        Test{
            v1: x,
            v2: y,
        }
    }
    fn func(&self) -> i32{
        println!("{}",self.v1);
        return self.v1
    }
}