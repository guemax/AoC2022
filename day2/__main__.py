#!/usr/bin/env python3

import numpy as np


def score(letter: str) -> int:
    if letter == "A" or letter == "X":
        return 1
    elif letter == "B" or letter == "Y":
        return 2
    elif letter == "C" or letter == "Z":
        return 3


def get_total_score(strategy_guide: str) -> int:
    total_score_of_game = 0

    for line in strategy_guide.splitlines():
        their_choice, my_choice = line.split(" ")

        if (their_choice == "A" and my_choice == "X") \
                or (their_choice == "B" and my_choice == "Y") \
                or (their_choice == "C" and my_choice == "Z"):
            total_score_of_game += score(my_choice) + 3
        elif (their_choice == "A" and my_choice == "Y") \
                or (their_choice == "B" and my_choice == "Z") \
                or (their_choice == "C" and my_choice == "X"):
            total_score_of_game += score(my_choice) + 6
        elif (their_choice == "A" and my_choice == "Z") \
                or (their_choice == "B" and my_choice == "X") \
                or (their_choice == "C" and my_choice == "Y"):
            total_score_of_game += score(my_choice)

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
