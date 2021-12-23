def parse_file(input_file):
    """
    Parse crab positions from a given file
    """
    with open(input_file, "r", encoding="utf-8") as fp:
        file_lines = [line.strip() for line in fp.readlines()]
    return list(map(int, file_lines[0].split(",")))


def triangle_number(n):
    """
    Return the nth triangle number
    """
    return (n * (n + 1)) // 2


def get_fuel_cost(crab_positions, destination):
    """
    Return the amount of fuel required to move all crabs
    to given destination when moving 1 unit costs 1 fuel
    """
    return sum([abs(p - destination) for p in crab_positions])


def get_fuel_cost_2(crab_positions, destination):
    """
    Return the amount of fuel required to move all crabs
    to given destination when moving 1 unit costs 1 fuel,
    moving 2 units costs 2 fuel, moving 3 units costs
    3 fuel, etc.
    """
    return sum([triangle_number(abs(p - destination)) for p in crab_positions])


def solution_1(input_file):
    crab_positions = parse_file(input_file)
    last_fuel_cost = float("inf")

    for destination in range(min(crab_positions), max(crab_positions) + 1):
        fuel_cost = get_fuel_cost(crab_positions, destination)
        if fuel_cost > last_fuel_cost:
            return last_fuel_cost
        last_fuel_cost = fuel_cost

    return last_fuel_cost


def solution_2(input_file):
    crab_positions = parse_file(input_file)
    last_fuel_cost = float("inf")

    for destination in range(min(crab_positions), max(crab_positions) + 1):
        fuel_cost = get_fuel_cost_2(crab_positions, destination)
        if fuel_cost > last_fuel_cost:
            return last_fuel_cost
        last_fuel_cost = fuel_cost

    return last_fuel_cost
