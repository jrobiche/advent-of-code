#!/usr/bin/env python3

from solution import solution_1, solution_2

if __name__ == "__main__":
    print("=== Part 1 ===")
    winner_score = solution_1("input.txt")
    print(f"First winner score: {winner_score}")

    print("=== Part 2 ===")
    winner_score = solution_2("input.txt")
    print(f"Last winner score: {winner_score}")
