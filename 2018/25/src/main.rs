use std::fs::read_to_string;

#[derive(PartialEq, Copy, Clone, Debug)]
struct Star(i32, i32, i32, i32);

impl Star {
    fn manhattan_distance_to_point(&self, p2: &Star) -> i32 {
        let x = self.0 - p2.0;
        let y = self.1 - p2.1;
        let z = self.2 - p2.2;
        let w = self.3 - p2.3;

        x.abs() + y.abs() + z.abs() + w.abs()
    }
}

fn convert_to_number(num_str: &str) -> i32 {
    num_str.parse::<i32>().unwrap()
}

fn parse_file(filename: &str) -> Vec<Star> {
    let read_lines = read_to_string(filename).expect("Failed to open the file");
    let mut stars: Vec<Star> = Vec::new();
    let lines = read_lines.split('\n').collect::<Vec<&str>>();

    for line in lines {
        let current_line = line.to_string();
        let line_split = current_line.split(',').collect::<Vec<&str>>();

        stars.push(Star(
            convert_to_number(line_split[0]),
            convert_to_number(line_split[1]),
            convert_to_number(line_split[2]),
            convert_to_number(line_split[3]),
        ));
    }

    stars
}

fn find_all_in_constellation(cs: &Star, li: &[Star], counted_stars: &mut Vec<Star>) {
    let current_star = cs.to_owned();
    let current_list = li.to_owned();
    let mut current_constellation: Vec<Star> = Vec::new();
    current_constellation.push(current_star);
    let mut iter = 0;

    loop {
        let star = current_constellation[iter];

        for star2 in current_list.iter() {
            if star.manhattan_distance_to_point(star2) <= 3
                && !current_constellation.contains(&star2)
            {
                current_constellation.push(*star2);
                if !counted_stars.contains(&star2) {
                    counted_stars.push(*star2);
                }
            }
        }

        if iter >= current_constellation.len() - 1 {
            break;
        }
        iter += 1;
    }
}

fn count_constellations(l: &[Star]) -> i32 {
    let mut count = 0;
    let current_list = l.to_owned();
    let mut counted_stars: Vec<Star> = Vec::new();
    let mut it = 0;

    while counted_stars.len() != current_list.len() || it < current_list.len() {
        if counted_stars.contains(&current_list[it]) {
            it += 1;
            continue;
        }
        let current_star = current_list[it];
        counted_stars.push(current_star);
        find_all_in_constellation(&current_star, &current_list, &mut counted_stars);
        count += 1;
        it += 1;
    }

    count
}

fn main() {
    let stars_list = parse_file("src/25.in");
    // part 1
    let diff_constellations = count_constellations(&stars_list);
    println!("{}", diff_constellations);
}
