#!/usr/bin/env python3

import numpy as np


def convert_letter_of_symbol_to_code(letter: str) -> np.int8:
    captial_c = 67
    offset_base = "A" if ord(letter) <= captial_c else "X"

    return np.int8(ord(letter) + 1 - ord(offset_base))


def get_total_score(strategy_guide: str) -> int:
    total_score_of_game = 0

    for line in strategy_guide.splitlines():
        their_choice, my_choice = list(map(convert_letter_of_symbol_to_code, line.split(" ")))
        print(f"{line} -> {their_choice}, {my_choice}", end="")

        if my_choice == their_choice:
            current_score = my_choice + 3
            print(f" === Score: {my_choice} + 3 == {current_score}")
        elif my_choice > their_choice:
            current_score = my_choice + 6
            print(f" === Score: {my_choice} + 6 == {current_score}")
        else:
            current_score = my_choice
            print(f" === Score: {my_choice} + 0 == {current_score}")

        total_score_of_game += current_score

    return total_score_of_game


def get_input(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


if __name__ == '__main__':
    print("\n======================")

    filenames = {"TEST INPUT": "day2/test_input.txt", "REAL INPUT": "day2/input.txt"}
    for type_of_input, filename in filenames.items():
        content = get_input(filename)
        total_score = get_total_score(content)

        print(f"\n{type_of_input}\n")
        print(f"--> Part 1: Total Score according to Strategy Guide: {total_score}.")
        print(f"--> Part 2: ")

    print("\n======================\n")
