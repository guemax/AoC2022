#!/usr/bin/env python3

import numpy as np


def from_letter_to_score(letter: str) -> int:
    character_code_for_capital_c = 67
    offset_base = "A" if ord(letter) <= character_code_for_capital_c else "X"
    return ord(letter) - ord(offset_base) + 1


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
        print(line)
        their_choice, my_choice = line.split(" ")
        """their_choice = from_letter_to_score(their_choice)
        my_choice = from_letter_to_score(my_choice)
        
        if their_choice == my_choice:
            total_score_of_game += my_choice + 3
        elif their_choice < my_choice:
            total_score_of_game += my_choice + 6
        else:
            total_score_of_game += my_choice
"""
        """
        A X -> 1 1
        B Y -> 2 2
        C Z -> 3 3
        
        A Y -> 1 2
        B Z -> 2 3
        C X -> 3 1
        
        A Z -> 1 3
        B X -> 2 1
        C Y -> 3 2
        """
        if from_letter_to_score(their_choice) == from_letter_to_score(my_choice):
            total_score_of_game += from_letter_to_score(my_choice) + 3
        elif (their_choice == "A" and my_choice == "Y") \
                or (their_choice == "B" and my_choice == "Z") \
                or (their_choice == "C" and my_choice == "X"):
            total_score_of_game += from_letter_to_score(my_choice) + 6
        elif (their_choice == "A" and my_choice == "Z") \
                or (their_choice == "B" and my_choice == "X") \
                or (their_choice == "C" and my_choice == "Y"):
            total_score_of_game += from_letter_to_score(my_choice)

    return total_score_of_game


def get_input(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


if __name__ == '__main__':
    print("\n======================")

    filenames = {"TEST INPUT": "day2/test_input.txt", "REAL INPUT": "day2/input.txt"}
    result = []
    for type_of_input, filename in filenames.items():
        content = get_input(filename)
        total_score = get_total_score(content)
        result.append(total_score)

        print(f"\n{type_of_input}\n")
        print(f"--> Part 1: Total Score according to Strategy Guide: {total_score}.")
        print(f"--> Part 2: ")

    assert result[0] == 15
    assert result[1] == 12458

    print("\n======================\n")
