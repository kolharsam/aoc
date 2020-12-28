use std::collections::VecDeque;

fn solve_eq(x_in: &i32, y_in: &i32) -> i32 {
    let x = x_in.to_owned();
    let y = y_in.to_owned();

    (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
}

fn is_wall_or_open(st: String) -> bool {
    let mut count_ones = 0;
    let str_split = st.split("").collect::<Vec<&str>>();

    for i in str_split.iter() {
        if *i == "1" {
            count_ones += 1;
        }
    }

    if count_ones % 2 != 0 {
        return false;
    }
    true
}

fn get_valid_neighbours(current_point: &(i32, i32), fav_num: &i32) -> Vec<(i32, i32)> {
    let mut valid_points: Vec<(i32, i32)> = Vec::new();
    let (x, y) = current_point;
    let dxs = [-1, 1, 0, 0];
    let dys = [0, 0, 1, -1];

    for i in 0..4 {
        let xx = x + dxs[i];
        let yy = y + dys[i];

        if xx < 0 || yy < 0 {
            continue;
        }

        let soln = solve_eq(&xx, &yy) + fav_num;
        let bin_soln = format!("{:b}", soln);
        if !is_wall_or_open(bin_soln) {
            continue;
        }

        valid_points.push((xx, yy));
    }

    valid_points
}

fn solve_maze(end_x: i32, end_y: i32, fav_num: i32) -> i32 {
    let start_x = 1;
    let start_y = 1;
    let mut q: VecDeque<(i32, i32)> = VecDeque::new();
    let mut visited: Vec<(i32, i32)> = Vec::new();
    let mut move_count = 0;
    let mut nodes_left_to_explore = 1;
    let mut nodes_in_next_layer = 0;
    let end_point = (end_x, end_y);

    q.push_back((start_x, start_y));
    visited.push((start_x, start_y));

    while !q.is_empty() {
        let current_point = q.pop_front().unwrap();
        if current_point == end_point {
            break;
        }

        // explore neighbours here
        let valid_neighbours = get_valid_neighbours(&current_point, &fav_num);
        for i in valid_neighbours.iter() {
            let (x_in, y_in) = i;
            if !visited.iter().any(|&p| p == (*x_in, *y_in)) {
                q.push_back((*x_in, *y_in));
                visited.push((*x_in, *y_in));
                nodes_in_next_layer += 1;
            }
        }

        nodes_left_to_explore -= 1;

        if nodes_left_to_explore == 0 {
            nodes_left_to_explore = nodes_in_next_layer;
            nodes_in_next_layer = 0;
            move_count += 1;
            // Part 2
            if move_count == 50 {
                println!("Part 2: {}", visited.len());
            }
        }
    }

    if move_count == 0 {
        return -1;
    }
    move_count
}

fn main() {
    let favorite_number = 1352;
    let reach_x = 31;
    let reach_y = 39;

    let least_steps = solve_maze(reach_x, reach_y, favorite_number);
    // part 1
    println!("Part 1: {}", least_steps);
}
