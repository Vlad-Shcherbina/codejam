use std::io::BufRead;

fn main() {
    let stdin = std::io::stdin();
    let mut it = stdin.lock().lines();
    let mut read_line = move || it.next().unwrap().unwrap();

    let n: i32 = read_line().parse().unwrap();
    for case_no in 0..n {
        let line = read_line();
        let mut it = line.split_whitespace();
        let n: usize = it.next().unwrap().parse().unwrap();
        let c: i32 = it.next().unwrap().parse().unwrap();
        assert!(it.next().is_none());

        let mut xs: Vec<usize> = (0..n).collect();
        let mut c = c - (n - 1) as i32;
        if c < 0 || c > (n * (n - 1) / 2) as i32 {
            println!("Case #{}: IMPOSSIBLE", case_no + 1);
            continue;
        }

        for i in (0..n - 1).rev() {
            let delta = c.min((n - 1 - i) as i32);
            xs[i..i + (delta + 1) as usize].reverse();
            c -= delta;
        }
        assert_eq!(c, 0);

        print!("Case #{}:", case_no + 1);
        for x in xs {
            print!(" {}", x + 1);
        }
        println!();
    }
}
