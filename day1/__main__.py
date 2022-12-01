#!/usr/bin/env python3

import numpy as np


def main(file: str):
    max_total_calories = 0
    current_total_calories = 0

    with open(file, "r") as f:
        for n, line in enumerate(f.readlines()):
            line = line.removesuffix("\n")
            print(f"Line {n}: {line}")
            if line == "":
                max_total_calories = max(current_total_calories, max_total_calories)
                current_total_calories = 0
                continue

            current_total_calories += int(line.removesuffix("\n"))

    return max_total_calories


if __name__ == '__main__':
    solution = main("day1/test_input.txt")
    print(f"The Elf with the most Calories is carrying {solution} Calories.")
