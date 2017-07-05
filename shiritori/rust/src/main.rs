use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::open("../BCCWJ_frequencylist_suw_ver1_0.tsv").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents);
    println!("Hello, world!");
    println!("{}", contents);
    
}
