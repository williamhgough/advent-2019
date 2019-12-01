def calculate_fuel(mass):
    return int((mass / 3)) - 2


def calculate_fuel_for_fuel(mass):
    x = calculate_fuel(mass)
    total = x
    while True:
        x = calculate_fuel(x)
        if x >= 0:
            total += x
        else:
            break
    return total


def process_inputs(lst, f):
    return [f(int(mass)) for mass in lst]


def part1(puzzle_input):
    return sum(process_inputs(puzzle_input, calculate_fuel))


def part2(puzzle_input):
    return sum(process_inputs(puzzle_input, calculate_fuel_for_fuel))


def __main__():
    with open("input.txt") as file:
        content = file.readlines()
        print("Part 1: {}".format(part1(content)))
        print("Part 2: {}".format(part2(content)))


if __name__ == "__main__":
    __main__()
