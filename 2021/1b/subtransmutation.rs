use std::io::BufRead;

fn main() {
    let stdin = std::io::stdin();
    let mut it = stdin.lock().lines();
    let mut read_line = move || it.next().unwrap().unwrap();

    let t: i32 = read_line().parse().unwrap();
    for case_no in 0..t {
        let line = read_line();
        let mut it = line.split_whitespace();
        let n: usize = it.next().unwrap().parse().unwrap();
        let a: usize = it.next().unwrap().parse().unwrap();
        let b: usize = it.next().unwrap().parse().unwrap();
        assert!(it.next().is_none());

        let us: Vec<i32> = read_line().split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        assert_eq!(us.len(), n);

        let mut sol = None;
        'outer: for start in us.len()..5000 {
            let mut xs = vec![0; start];
            xs.push(1);
            while xs.len() > 1 {
                let cnt = xs.pop().unwrap();
                let i = xs.len();
                let m = us.get(i - 1).copied().unwrap_or_default();
                if cnt < m {
                    continue 'outer;
                }
                let excess = (cnt - m).min(10000);
                if excess > 0 {
                    if i > a {
                        xs[i - a] += excess;
                    }
                    if i > b {
                        xs[i - b] += excess;
                    }                    
                }
            }
            sol = Some(start);
            break;
        }
        print!("Case #{}: ", case_no + 1);
        match sol {
            Some(n) => println!("{}", n),
            None => println!("IMPOSSIBLE"),
        }        
    }
}
