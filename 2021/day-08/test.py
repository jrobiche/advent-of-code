#!/usr/bin/env python3

from solution import solution_1, solution_2

if __name__ == "__main__":
    assert solution_1("test_input.txt") == 26
    assert solution_2("test_input_2.txt") == 5353
    assert solution_2("test_input.txt") == 61229
    print("All tests passed successfully")
