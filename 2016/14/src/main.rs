extern crate md5;
use md5::compute;

fn has_three_in_row(strg: &str) -> (bool, String) {
    let current = strg.to_owned();
    let current_string = current.split("").collect::<Vec<&str>>();
    let mut index = 0;

    while index < current_string.len() - 2 {
        if current_string[index] == current_string[index + 1]
            && current_string[index] == current_string[index + 2]
        {
            return (true, current_string[index].to_string());
        }
        index += 1;
    }

    (false, "".to_string())
}

fn has_five(strg: String, ch: String) -> bool {
    let current_string = strg.split("").collect::<Vec<&str>>();
    let mut index = 0;

    while index < current_string.len() - 4 {
        if current_string[index] == ch
            && current_string[index + 1] == ch
            && current_string[index + 2] == ch
            && current_string[index + 3] == ch
            && current_string[index + 4] == ch
        {
            return true;
        }
        index += 1;
    }

    false
}

fn has_five_in_row(strg: &str, index: i32, ch: String, is_p2: bool) -> bool {
    let current_string = strg.to_owned();
    let mut current_index = index + 1;

    while current_index <= index + 1000 {
        let current_str = format!("{}{}", current_string, current_index);
        let mut current_hash_digest = compute(&current_str);
        if is_p2 {
            current_hash_digest = compute_stretched_hash(&current_str);
        }
        let current_hash = format!("{:x}", current_hash_digest);

        if has_five(current_hash, ch.to_owned()) {
            return true;
        }

        current_index += 1;
    }

    false
}

fn is_valid_hash(bstr: &str, ci: &i32, rounds: i32) -> bool {
    let base_str = bstr.to_owned();
    let current_index = ci.to_owned();

    let current_str = format!("{}{}", base_str, current_index);
    let mut current_hash_digest = compute(&current_str);
    if rounds == 2017 {
        current_hash_digest = compute_stretched_hash(&current_str);
    }
    let current_hash = format!("{:x}", current_hash_digest);
    let (has_three, ch) = has_three_in_row(&current_hash);

    if !has_three {
        return false;
    }

    if has_five_in_row(&base_str, current_index, ch, rounds == 2017) {
        return true;
    }

    false
}

fn compute_stretched_hash(st: &str) -> md5::Digest {
    let base_string = st.to_owned();
    let mut current_hash = compute(base_string);
    let mut count = 0;

    loop {
        let current_hash_str = format!("{:x}", &current_hash);
        current_hash = compute(current_hash_str);
        count += 1;
        if count == 2016 {
            break;
        }
    }

    current_hash
}

fn find_hash_index(base: &str, rounds: i32) -> i32 {
    let mut index = 0;
    let mut count = 0;

    loop {
        println!("here: {}", index);
        if is_valid_hash(base, &index, rounds) {
            println!("Found!: {} {}", index, count);
            count += 1;
            if count == 64 {
                break;
            }
        }
        index += 1;
    }

    index
}

fn main() {
    // NOTE: this is extremely inefficient and slow.
    let base = "ngcjuoqr";
    // part 1
    println!("{}", find_hash_index(&base, 1));
    // part 2
    println!("{}", find_hash_index(&base, 2017));
}
