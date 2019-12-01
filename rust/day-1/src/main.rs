use std::fs;

fn main() {
    let contents =
        fs::read_to_string("input/input.txt").expect("Something went wrong reading the file");
    let iter: Vec<&str> = contents.split('\n').collect();
    let mut first_total: i32 = 0;
    let mut second_total: i32 = 0;
    for i in iter {
        let int_i = i.parse().unwrap();
        first_total += calculate_fuel(int_i);
        second_total += calculate_fuel_for_fuel(int_i);
    }
    println!("Part 1 fuel total: {}", first_total);
    println!("Part 2 fuel total: {}", second_total);
}

fn calculate_fuel(mass: i32) -> i32 {
    (mass / 3) as i32 - 2
}

fn calculate_fuel_for_fuel(mass: i32) -> i32 {
    let mut x: i32 = calculate_fuel(mass);
    let mut total: i32 = x;
    loop {
        x = calculate_fuel(x);
        if x < 0 {
            break;
        }
        total += x
    }
    total
}
