fn replace_bits(current: &[String]) -> Vec<String> {
    let mut bits = current.to_owned();
    let mut point = 0;

    while point < bits.len() {
        let one = "1".to_string();
        let zero = "0".to_string();
        if bits[point] == zero {
            bits[point] = one;
        } else {
            bits[point] = zero;
        }
        point += 1;
    }

    bits
}

fn run_dragon_curve(start_str: &str, disk: &i32) -> Vec<String> {
    let st_str = start_str.to_owned();
    let str_split = st_str.split("").collect::<Vec<&str>>();
    let mut dragon_str: Vec<String> = Vec::new();

    for st in str_split {
        if st != "" {
            dragon_str.push(st.to_string());
        }
    }

    let mut len = dragon_str.len();

    while len <= *disk as usize {
        let mut dragon_copy = dragon_str.clone();
        dragon_copy.reverse();
        dragon_copy = replace_bits(&dragon_copy);
        dragon_str.push("0".to_string());
        for d in dragon_copy {
            dragon_str.push(d);
        }
        len = dragon_str.len();
    }

    dragon_str[0..(*disk as usize)].to_vec()
}

fn trim_checksum(check_vec: &[String]) -> Vec<String> {
    let c_sum = check_vec.to_owned();
    let mut checksum: Vec<String> = Vec::new();
    let mut iter = 0;

    while iter < c_sum.len() {
        if c_sum[iter] == c_sum[iter + 1] {
            checksum.push("1".to_string());
        } else {
            checksum.push("0".to_string());
        }
        iter += 2;
    }

    checksum
}

fn run_dragon_checksum(result: &[String]) -> Vec<String> {
    let c_sum = result.to_owned();
    let mut checksum = c_sum;

    let mut len = checksum.len();

    while len % 2 == 0 {
        checksum = trim_checksum(&checksum);
        len = checksum.len();
    }

    checksum
}

fn main() {
    let start = "10111011111001111";
    let disk_space = 272;
    // for part 2
    let disk_space_2 = 35651584;

    let mut dragon_result = run_dragon_curve(&start, &disk_space);
    let mut checksum = run_dragon_checksum(&dragon_result);
    // part 1
    println!("{}", checksum.join(""));

    dragon_result = run_dragon_curve(&start, &disk_space_2);
    checksum = run_dragon_checksum(&dragon_result);
    // part 2 - takes a lot of time
    println!("{}", checksum.join(""));
}
