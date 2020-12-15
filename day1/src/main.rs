fn find_pair_who_sum_to(l: Vec<i32>, v:i32) -> Option<(i32, i32)>{
    for i in 0..l.len(){
        for j in (i+1)..l.len() {
            if l[i] + l[j] == v {
                return Some((l[i], l[j]));
            }
        }
    }
    None
}

fn main() {
    let pairs = find_pair_who_sum_to(include_str!("in.txt")
        .split('\n')
        .map(str::parse::<i32>)
        .map(Result::unwrap)
        .collect(), 2020);

    if let Some((a, b)) = pairs {
        println!("{}", a+b);
        println!("{}", a*b);
    }
    // dbg!(pairs);
}
