#!/usr/bin/env python3

import numpy as np


def convert_letter_of_symbol_to_code(letter: str) -> np.int8:
    captial_c = 67
    offset_base = "A" if ord(letter) <= captial_c else "X"

    return np.int8(ord(letter) + 1 - ord(offset_base))


def get_total_score(strategy_guide: str) -> np.int_:
    total_score = 0
    for round in strategy_guide.splitlines():
        their_choice, my_choice = list(map(convert_letter_of_symbol_to_code, round.split(" ")))

        delta = my_choice - their_choice
        total_score += my_choice
        if delta == 0:
            print("Draw")
            total_score += 3
        elif delta > 0:
            print("You won")
            total_score += 6
        else:
            print("You lose")

    return total_score


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
