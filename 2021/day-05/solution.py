#!/usr/bin/env python3


def is_line_diagonal(line):
    return not (is_line_horizontal(line) or is_line_vertical(line))


def is_line_horizontal(line):
    return line[0][1] == line[1][1]


def is_line_vertical(line):
    return line[0][0] == line[1][0]


def parse_file(input_file):
    def parse_coordinates_str(coordinates_str):
        coordinates = coordinates_str.split(",")
        coordinates = map(int, coordinates)
        return tuple(coordinates)

    with open(input_file, "r", encoding="utf-8") as fp:
        file_lines = [line.strip() for line in fp.readlines()]

    lines = []

    for line in file_lines:
        partitions = line.partition(" -> ")
        start_coordinates = parse_coordinates_str(partitions[0])
        stop_coordinates = parse_coordinates_str(partitions[-1])
        lines.append((start_coordinates, stop_coordinates))

    return lines


def graph_point(point, graph):
    key = ",".join(map(str, point))
    if key in graph:
        graph[key] += 1
    else:
        graph[key] = 1
    return


def graph_diagonal_line(line, graph):
    x_delta = 1 if line[0][0] < line[1][0] else -1
    y_delta = 1 if line[0][1] < line[1][1] else -1

    x_start = min(line[0][0], line[1][0])
    x_stop = max(line[0][0], line[1][0])
    x_range = range((x_stop - x_start) + 1)

    for i in x_range:
        x = line[0][0] + (i * x_delta)
        y = line[0][1] + (i * y_delta)
        graph_point((x, y), graph)
    return


def graph_horizontal_line(line, graph):
    x_start = min(line[0][0], line[1][0])
    x_stop = max(line[0][0], line[1][0])
    y = line[0][1]
    for x in range(x_start, x_stop + 1):
        graph_point((x, y), graph)
    return


def graph_vertical_line(line, graph):
    y_start = min(line[0][1], line[1][1])
    y_stop = max(line[0][1], line[1][1])
    x = line[0][0]
    for y in range(y_start, y_stop + 1):
        graph_point((x, y), graph)
    return


def solution_1(input_file):
    lines = parse_file(input_file)
    horizontal_lines = list(filter(is_line_horizontal, lines))
    vertical_lines = list(filter(is_line_vertical, lines))

    graph = {}

    for line in horizontal_lines:
        graph_horizontal_line(line, graph)

    for line in vertical_lines:
        graph_vertical_line(line, graph)

    return sum(1 for v in graph.values() if v >= 2)


def solution_2(input_file):
    lines = parse_file(input_file)
    horizontal_lines = list(filter(is_line_horizontal, lines))
    vertical_lines = list(filter(is_line_vertical, lines))
    diagonal_lines = list(filter(is_line_diagonal, lines))

    graph = {}

    for line in horizontal_lines:
        graph_horizontal_line(line, graph)

    for line in vertical_lines:
        graph_vertical_line(line, graph)

    for line in diagonal_lines:
        graph_diagonal_line(line, graph)

    return sum(1 for v in graph.values() if v >= 2)
