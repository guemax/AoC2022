#!/usr/bin/env python3

import numpy as np


def get_list_of_total_calories_of_top_three_elves_with_the_most_calories(inventory_list: str) -> list:
    list_of_total_calories_of_all_elves = []

    for individual_calories_of_this_elf in inventory_list.split("\n\n"):
        total_calories_of_this_elf = np.fromstring(individual_calories_of_this_elf, dtype=np.int_, sep="\n").sum()
        list_of_total_calories_of_all_elves.append(total_calories_of_this_elf)

    list_of_total_calories_of_all_elves.sort()
    return list_of_total_calories_of_all_elves[-3:]


def get_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == '__main__':
    test_input = "day1/test_input.txt"
    input_ = "day1/input.txt"

    test_content = get_input(test_input)
    real_content = get_input(input_)

    print("\n===== TEST INPUT =====\n")

    calories_of_top_three_elves = get_list_of_total_calories_of_top_three_elves_with_the_most_calories(test_content)

    print(f"The Elf with the most Calories is carrying {max(calories_of_top_three_elves)} Calories.")
    print(f"The top three Elves are carrying {sum(calories_of_top_three_elves)} Calories in total.")

    print("\n===== REAL INPUT =====")

    calories_of_top_three_elves = get_list_of_total_calories_of_top_three_elves_with_the_most_calories(real_content)
    print(f"The Elf with the most Calories is carrying {max(calories_of_top_three_elves)} Calories.")
    print(f"The top three Elves are carrying {sum(calories_of_top_three_elves)} Calories in total.")
    print("\n======================\n")
