#!/usr/bin/env python3

from collections import namedtuple

Command = namedtuple("Command", ["direction", "units"])


def parse_file_lines(file_lines):
    commands = []
    for line in file_lines:
        direction, units = line.split(" ")
        units = int(units)
        command = Command(direction, units)
        commands.append(command)
    return commands


def perform_command(command, position):
    horizontal_delta = 0
    depth_delta = 0
    if command.direction == "forward":
        horizontal_delta = command.units
    elif command.direction == "up":
        depth_delta = -1 * command.units
    elif command.direction == "down":
        depth_delta = command.units
    position["horizontal"] += horizontal_delta
    position["depth"] += depth_delta
    return


def perform_command_2(command, position):
    horizontal_delta = 0
    depth_delta = 0
    aim_delta = 0
    if command.direction == "forward":
        horizontal_delta = command.units
        depth_delta = position["aim"] * command.units
    elif command.direction == "up":
        aim_delta = -1 * command.units
    elif command.direction == "down":
        aim_delta = command.units
    position["horizontal"] += horizontal_delta
    position["depth"] += depth_delta
    position["aim"] += aim_delta
    return


def main():
    # input_file = "test_input.txt"
    input_file = "input.txt"

    with open(input_file, encoding="utf-8") as fp:
        file_lines = [line.strip() for line in fp.readlines()]

    commands = parse_file_lines(file_lines)

    print("=== Part 1 ===")
    position = {
        "horizontal": 0,
        "depth": 0,
    }
    for command in commands:
        perform_command(command, position)
    solution_1 = position["horizontal"] * position["depth"]
    print(f"Product of horizontal position and depth: {solution_1}")

    print("=== Part 2 ===")
    position = {
        "horizontal": 0,
        "depth": 0,
        "aim": 0,
    }
    for command in commands:
        perform_command_2(command, position)
    solution_2 = position["horizontal"] * position["depth"]
    print(f"Product of horizontal position and depth: {solution_2}")


if __name__ == "__main__":
    main()
