#!/usr/bin/env python3
"""Combinations:
a && x == draw -> 1 1
b && y == draw -> 2 2
c && z == draw -> 3 3

a && y == win -> 1 2 d1 pos
b && z == win -> 2 3 d1 pos
c && x == win -> 3 1 d2 pos

a && z == loss -> 1 3 d2 neg
b && x == loss -> 2 1 d1 neg
c && y == loss -> 3 2 d1 neg
"""
import numpy as np


def convert_letter_of_symbol_to_code(letter: str) -> np.int8:
    if letter == "A" or letter == "X":
        return np.int8(1)
    elif letter == "B" or letter == "Y":
        return np.int8(2)
    elif letter == "C" or letter == "Z":
        return np.int8(3)


def get_total_score(strategy_guide: str) -> np.int_:
    total_score = 0
    for round in strategy_guide.splitlines():
        print(round)
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
