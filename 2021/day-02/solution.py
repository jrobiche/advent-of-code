#!/usr/bin/env python3

from collections import namedtuple

Command = namedtuple("Command", ["direction", "units"])


def parse_file(input_file):
    with open(input_file, encoding="utf-8") as fp:
        file_lines = [line.strip() for line in fp.readlines()]
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


def solution_1(input_file):
    commands = parse_file(input_file)
    position = {
        "horizontal": 0,
        "depth": 0,
    }
    for command in commands:
        perform_command(command, position)
    return position["horizontal"] * position["depth"]


def solution_2(input_file):
    commands = parse_file(input_file)
    position = {
        "horizontal": 0,
        "depth": 0,
        "aim": 0,
    }
    for command in commands:
        perform_command_2(command, position)
    return position["horizontal"] * position["depth"]
