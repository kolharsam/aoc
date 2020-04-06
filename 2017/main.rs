// const FORTY_MIL: i64 = 40000000;
const FIVE_MIL: i64 = 5000000;

fn convert_to_binary(n: i64) -> Vec<i64> {
    let mut vec : Vec<i64> = vec![0; 32];

    let mut iter = n;
    let mut steps = 0;

    while iter > 0 {
        if iter % 2 == 1 {
            vec[steps] = 1;
        }
        
        iter = iter / 2;
        steps+=1;
    }

    vec.reverse();

    vec
}

fn get_last_16(vec: Vec<i64>) -> Vec<i64> {
    let mut rev_vec = vec;
    rev_vec.reverse();

    let mut res_vec = vec![0; 16];

    let mut iter = 0;

    while iter < 16 {
        let current_element = rev_vec[iter];

        res_vec[iter] = current_element;
        iter+=1;
    }

    res_vec.reverse();

    res_vec
}

fn is_vec_equal(a: Vec<i64>, b: Vec<i64>) -> bool {
    a == b
}

fn gen_a(start: i64, n: i64) -> Vec<i64> {
    let mut val_pointer : i64 = start;
    let mut iter : i64 = n;
    
    let gen_a_const : i64 = 16807;
    let mut gen_vec = vec![];

    while iter > 0 {
        let mul_factor : i64 = (val_pointer * gen_a_const) as i64;
        val_pointer = mul_factor % 2147483647;
        if val_pointer % 4 == 0 {
            gen_vec.push(val_pointer);
            iter-=1;
        }
    }

    gen_vec
}


fn gen_b(start: i64, n: i64) -> Vec<i64> {
    let mut val_pointer = start;
    let mut iter : i64 = n;
    let gen_b_const : i64 = 48271;

    let mut gen_vec = vec![];

    while iter > 0 {
        let mul_factor : i64 = (val_pointer * gen_b_const) as i64;
        val_pointer = mul_factor % 2147483647;
        if val_pointer % 8 == 0 {
            gen_vec.push(val_pointer);
            iter-=1;
        }
    }

    gen_vec
}

fn get_last_16_bin_list(vec: Vec<i64>) -> Vec<Vec<i64>> {
    let in_vec : Vec<i64> = vec;

    let mut res_vec: Vec<Vec<i64>> = vec![];
    let mut iter = 0;

    while iter < FIVE_MIL {
        let current_element = in_vec[iter as usize];
        let bin_num = convert_to_binary(current_element);
        let last_16 = get_last_16(bin_num);
        res_vec.push(last_16);
        
        if iter % 200000 == 0 {
            println!("HEY! {}", iter);
        } 

        iter += 1;
    }

    res_vec
}

fn get_eq_list (a: Vec<Vec<i64>>, b: Vec<Vec<i64>>) -> i64 {
    let mut iter = 0;
    let mut match_vec = 0;

    println!("Matching now!");

    while iter < FIVE_MIL {
        let current_a_element = &a[iter as usize];
        let current_b_element = &b[iter as usize];

        if is_vec_equal(current_a_element.to_vec(), current_b_element.to_vec()) {
            match_vec+=1;
        }

        iter+=1;
    }

    match_vec
}

fn main() {
    // Problem Input : a => 591 b => 393
    let gen_a_list = gen_a(591, FIVE_MIL);
    println!("Generated List A!");
    let gen_b_list = gen_b(393, FIVE_MIL);
    println!("Generated List B!");

    let gen_a_bin_list = get_last_16_bin_list(gen_a_list);
    println!("Generated List BIN A!");
    let gen_b_bin_list = get_last_16_bin_list(gen_b_list);
    println!("Generated List BIN B!");

    let gen_match_list = get_eq_list(gen_a_bin_list, gen_b_bin_list);

    println!("Matched Cases: {}", gen_match_list);
}
