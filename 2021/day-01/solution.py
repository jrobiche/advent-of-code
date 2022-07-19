#!/usr/bin/env python3


def parse_file(input_file):
    with open(input_file, encoding="utf-8") as fp:
        ints = [int(line.strip()) for line in fp.readlines()]
    return ints


def count_increases(int_list, window_size=1):
    count = 0
    stop_index = len(int_list) - window_size
    for i in range(stop_index):
        window_1 = int_list[i : (i + window_size)]
        window_1_sum = sum(window_1)

        window_2 = int_list[(i + 1) : (i + 1 + window_size)]
        window_2_sum = sum(window_2)

        if window_1_sum < window_2_sum:
            count += 1
    return count


def solution_1(input_file):
    ints = parse_file(input_file)
    return count_increases(ints)


def solution_2(input_file):
    ints = parse_file(input_file)
    return count_increases(ints, window_size=3)
