#!/usr/bin/env python3

import numpy as np


def get_max_total_calories(content: str) -> np.int_:
    sum_of_calories = []

    for line in content.split("\n\n"):
        sum_of_calories.append(np.fromstring(line, dtype=np.int_, sep="\n").sum())

    return max(sum_of_calories)


def get_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def get_max_total_calories_of_top_three(file: str):
    max_calories = 0
    current_calories = 0
    total_calories_of_each_elf = []
    content = get_input(file)

    for line in content.splitlines():
        if line != "":
            current_calories += int(line)
            continue

        max_calories = max(current_calories, max_calories)
        total_calories_of_each_elf.append(current_calories)

        current_calories = 0

    total_calories_of_each_elf.append(current_calories)
    return sum(total_calories_of_each_elf[-3:])


if __name__ == '__main__':
    test_input = "day1/test_input.txt"
    input_ = "day1/input.txt"

    test_content = get_input(test_input)
    real_content = get_input(input_)

    print("\n===== TEST INPUT =====\n")

    solution = get_max_total_calories(test_content)
    solution_part2 = get_max_total_calories_of_top_three(test_input)

    print(f"The Elf with the most Calories is carrying {solution} Calories.")
    print(f"The top three Elves are carrying {solution_part2} Calories in total.")

    print("\n===== REAL INPUT =====")
    solution = get_max_total_calories(real_content)
    solution_part2 = get_max_total_calories_of_top_three(input_)

    print(f"The Elf with the most Calories is carrying {solution} Calories.")
    print(f"The top three Elves are carrying {solution_part2} Calories in total.")
    print("\n======================\n")
