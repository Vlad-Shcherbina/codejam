use std::io::BufRead;

fn main() {
    let stdin = std::io::stdin();
    let mut it = stdin.lock().lines();
    let mut read_line = move || it.next().unwrap().unwrap();

    let line = read_line();
    let mut it = line.split_whitespace();
    let t: i32 = it.next().unwrap().parse().unwrap();
    let n: usize = it.next().unwrap().parse().unwrap();
    let _q: i32 = it.next().unwrap().parse().unwrap();

    for _case_no in 0..t {
        let mut xs = vec![1, 2, 3];
        println!("1 2 3");
        let med: usize = read_line().parse().unwrap();
        xs.swap(1, med - 1);
        for i in 4..=n {
            let mut left = 0;
            let mut right = xs.len();
            while right - left >= 2 {
                let m1 = (2 * left + right) / 3;
                let m2 = (left + 2 * right) / 3;
                println!("{} {} {}", xs[m1], xs[m2], i);
                let mid: usize = read_line().parse().unwrap();
                if mid == xs[m1] {
                    right = m1;
                } else if mid == xs[m2] {
                    left = m2 + 1;
                } else if mid == i {
                    left = m1 + 1;
                    right = m2;
                } else {
                    panic!();
                }                
            }
            if left < right {
                if left > 0 {
                    println!("{} {} {}", xs[left - 1], xs[left], i);
                    let mid: usize = read_line().parse().unwrap();
                    if mid == xs[left] {
                        left += 1;
                    } else if mid == i {
                        right = left;
                    } else {
                        panic!();
                    }
                } else {
                    println!("{} {} {}", xs[left], xs[left + 1], i);
                    let mid: usize = read_line().parse().unwrap();
                    if mid == xs[left] {
                        right = left;
                    } else if mid == i {
                        left += 1;
                    } else {
                        panic!();
                    }
                }
            }
            assert_eq!(left, right);
            xs.insert(left, i);
        }
        print!("{}", xs[0]);
        for &x in &xs[1..] {
            print!(" {}", x);
        }
        println!();
        let verdict: i32 = read_line().parse().unwrap();
        assert_eq!(verdict, 1);
    }
}
