use std::fs::read_to_string;

#[derive(Debug, Clone, Copy, PartialEq)]
struct Coords(i64, i64, i64);

#[derive(Debug, Copy, Clone)]
struct NanoBot {
    position: Coords,
    radius: i64,
}

fn convert_to_number(s: &str) -> i64 {
    s.to_owned().parse::<i64>().unwrap()
}

fn parse_coords(coord_split: &str) -> Coords {
    let c_str = coord_split.to_owned();
    let c_str_split = c_str.split("=<").collect::<Vec<&str>>();
    let c_split_str = c_str_split[1].to_string();
    let point = c_split_str.split('>').collect::<Vec<&str>>()[0];
    let pointc = point.to_string();
    let points = pointc.split(',').collect::<Vec<&str>>();

    Coords(
        convert_to_number(points[0]),
        convert_to_number(points[1]),
        convert_to_number(points[2]),
    )
}

fn parse_radius(rad: &str) -> i64 {
    let rad_str = rad.to_owned();
    let rad_split = rad_str.split('=').collect::<Vec<&str>>();
    convert_to_number(rad_split[1])
}

fn parse_file(filename: &str) -> Vec<NanoBot> {
    let read_lines = read_to_string(filename).expect("Failed to open file");
    let lines = read_lines.split('\n').collect::<Vec<&str>>();
    let mut bots: Vec<NanoBot> = Vec::new();

    for line in lines {
        let line_str = line.to_string();
        let line_split = line_str.split(", ").collect::<Vec<&str>>();
        let coords = parse_coords(line_split[0]);
        let radius = parse_radius(line_split[1]);
        bots.push(NanoBot {
            position: coords,
            radius,
        });
    }

    bots
}

fn manhattan_distance(p1: &Coords, p2: &Coords) -> i64 {
    let x: i64 = p1.0 - p2.0;
    let y: i64 = p1.1 - p2.1;
    let z: i64 = p1.2 - p2.2;

    x.abs() + y.abs() + z.abs()
}

fn get_max_range_point(bl: &[NanoBot]) -> NanoBot {
    let mut max_range = 0;
    let mut index = 0;

    for (ind, bot) in bl.iter().enumerate() {
        if bot.radius > max_range {
            max_range = bot.radius;
            index = ind;
        }
    }

    bl[index]
}

fn get_points_in_range(bl: &[NanoBot]) -> i32 {
    let mut count = 0;
    let max_range_point = get_max_range_point(bl);

    for bot in bl {
        if bot.position == max_range_point.position {
            count += 1;
            continue;
        }
        let dis = manhattan_distance(&bot.position, &max_range_point.position);
        if dis <= max_range_point.radius {
            count += 1;
        }
    }

    count
}

/**
 * References for part 2
 * https://github.com/fuglede/adventofcode/blob/master/2018/day23/solutions.py
 * https://todd.ginsberg.com/post/advent-of-code/2018/day23/
 */

fn main() {
    let bots_list = parse_file("src/23-sample.in");
    let num_in_range = get_points_in_range(&bots_list);
    // part 1
    println!("{}", num_in_range);
}
