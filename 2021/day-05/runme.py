#!/usr/bin/env python3

from solution import solution_1, solution_2

if __name__ == "__main__":
    print("=== Part 1 ===")
    result = solution_1("input.txt")
    print(f"Points with 2 or more intersecting lines: {result}")

    print("=== Part 2 ===")
    result = solution_2("input.txt")
    print(f"Points with 2 or more intersecting lines: {result}")
