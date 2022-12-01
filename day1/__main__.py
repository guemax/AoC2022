#!/usr/bin/env python3

import numpy as np


def get_list_of_total_calories_of_top_three_elves_with_the_most_calories(inventory_list: str) -> list:
    list_of_total_calories_of_all_elves = []

    for individual_calories_of_this_elf in inventory_list.split("\n\n"):
        total_calories_of_this_elf = np.fromstring(individual_calories_of_this_elf, dtype=np.int_, sep="\n").sum()
        list_of_total_calories_of_all_elves.append(total_calories_of_this_elf)

    list_of_total_calories_of_all_elves.sort()
    return list_of_total_calories_of_all_elves[-3:]


def get_input(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


if __name__ == '__main__':
    print("\n======================")

    filenames = {"TEST INPUT": "day1/test_input.txt", "REAL INPUT": "day1/input.txt"}
    for type_of_input, filename in filenames.items():
        content = get_input(filename)
        calories_of_top_three_elves = get_list_of_total_calories_of_top_three_elves_with_the_most_calories(content)

        print(f"\n{type_of_input}\n")
        print(f"--> Part 1: The N°1 Elf is carrying {max(calories_of_top_three_elves)} Calories in total.")
        print(f"--> Part 2: The TOP 3 Elves are carrying {sum(calories_of_top_three_elves)} Calories in total.")

    print("\n======================\n")
