/**
* Problem: Consecutive Prime Sum
* Statement:
*
* The prime 41, can be written as the sum of six consecutive primes:
* 41 = 2 + 3 + 5 + 7 + 11 + 13
* This is the longest sum of consecutive primes that adds to a prime below one-hundred.
* The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

* Which prime, below one-million, can be written as the sum of the most consecutive primes?
*/

type PrimeList = Vec<(i32, i32)>;

fn is_prime(num: i32) -> bool {
    if num % 2 == 0 {
        return false;
    }

    for i in 3..=((num as f64).sqrt() as i32) {
        if i % 2 == 0 {
            continue;
        }
        if num % i == 0 {
            return false;
        }
    }

    true
}

fn get_num_list(num: i32) -> Vec<i32> {
    let mut new_prime_num_list: Vec<i32> = Vec::new();

    new_prime_num_list
}

fn find_prime_sum(num: i32) -> Option<(i32, i32)> {
    let all_primes_before_num = get_num_list(num);
    None
}

fn get_longest_consecutive_sequence(num: i32) -> (i32, i32) {
    let mut prime_list: PrimeList = Vec::new();

    for i in 11..=num {
        if is_prime(i) {
            let ps = find_prime_sum(i);
            match ps {
                Some(val) => prime_list.push(val),
                None => continue,
            }
        }
    }

    prime_list.sort_by_key(|k| k.1);

    prime_list[0]
}

fn main() {
    println!("{:?}", get_longest_consecutive_sequence(100));
}
