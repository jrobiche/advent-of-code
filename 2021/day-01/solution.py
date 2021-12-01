#!/usr/bin/env python3


def count_increases(int_list, window_size=1):
    count = 0
    stop_index = len(int_list) - window_size
    for i in range(stop_index):
        window_1 = int_list[i:(i + window_size)]
        window_1_sum = sum(window_1)

        window_2 = int_list[(i + 1):(i + 1 + window_size)]
        window_2_sum = sum(window_2)

        if window_1_sum < window_2_sum:
            count += 1
    return count


def main():
    # input_file = "test_input.txt"
    input_file = "input.txt"

    with open(input_file, encoding="utf-8") as fp:
        file_lines = [line.strip() for line in fp.readlines()]

    print("=== Part 1 ===")
    ints = [int(line) for line in file_lines]
    increase_count = count_increases(ints)
    print(f"Increase count: {increase_count}")

    print("=== Part 2 ===")
    increase_count = count_increases(ints, window_size=3)
    print(f"Increase count: {increase_count}")


if __name__ == "__main__":
    main()
