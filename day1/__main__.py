#!/usr/bin/env python3

import numpy as np


def get_max_total_calories(content: str) -> np.int_:
    list_of_summed_calories = []

    for this_elfs_calories_as_str in content.split("\n\n"):
        this_elfs_calories = np.fromstring(this_elfs_calories_as_str, dtype=np.int_, sep="\n")
        sum_of_this_elfs_calories = this_elfs_calories.sum()

        list_of_summed_calories.append(sum_of_this_elfs_calories)

    return max(list_of_summed_calories)


def get_list_of_total_calories_of_top_three_elves_with_the_most_calories(inventory_list: str) -> list:
    list_of_total_calories_of_all_elves = []

    for individual_calories_of_this_elf in inventory_list.split("\n\n"):
        total_calories_of_this_elf = np.fromstring(individual_calories_of_this_elf, dtype=np.int_, sep="\n").sum()
        list_of_total_calories_of_all_elves.append(total_calories_of_this_elf)

    return list_of_total_calories_of_all_elves.sort()[-3:]


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
