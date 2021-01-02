fn break_digits(num: &i32) -> Vec<i32> {
    let mut digits: Vec<i32> = Vec::new();
    let mut lim = num.to_owned();

    while lim > 0 {
        digits.push(lim % 10);
        lim /= 10;
    }

    digits.reverse();

    digits
}

fn make_recipes(num: &i32) -> (String, i32) {
    let num_digits = break_digits(num);
    let mut one = 3;
    let mut two = 7;
    let mut current_pos_one = 0;
    let mut current_pos_two = 1;
    let mut num_vec: Vec<i32> = Vec::new();
    let mut p1: Vec<i32> = Vec::new();
    num_vec.push(one);
    num_vec.push(two);
    let lim = *num + 10;

    loop {
        let current_sum = one + two;
        if current_sum >= 10 {
            let digits = break_digits(&current_sum);
            for digit in digits {
                num_vec.push(digit);
            }
        } else {
            num_vec.push(current_sum);
        }

        let current_len = num_vec.len() as i32;
        current_pos_one = (1 + one + current_pos_one) % current_len;
        current_pos_two = (1 + two + current_pos_two) % current_len;
        one = num_vec[current_pos_one as usize];
        two = num_vec[current_pos_two as usize];

        if current_len == lim {
            p1 = num_vec[(*num as usize)..((*num + 10) as usize)].to_vec();
        }

        if current_len > num_digits.len() as i32 {
            let sub_vec =
                num_vec[((current_len - 7) as usize)..((current_len - 1) as usize)].to_vec();
            if sub_vec == num_digits {
                return (
                    p1.iter().map(|x| x.to_string()).collect::<String>(),
                    current_len - 7,
                );
            }
        }
    }
}

fn main() {
    let input = 260321;
    let (p1, p2) = make_recipes(&input);
    println!("{}\n{}", p1, p2);
}
