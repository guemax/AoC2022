#!/usr/bin/env python3


def get_total_score(strategy_guide: str) -> int:
    total_score_of_game = 0

    for line in strategy_guide.splitlines():
        print(line, end="")
        line = line.split(" ")
        their_choice, expected_outcome = from_letter_to_score_of_move(line[0]), from_letter_to_expected_outcome(line[1])
        print(f" : {their_choice}, {expected_outcome}")

        if expected_outcome == 3:
            total_score_of_game += their_choice
        elif expected_outcome == 6:
            my_choice = 0
            if their_choice == 1:  # Rock
                my_choice = 2  # Paper
            elif their_choice == 2:  # Paper
                my_choice = 3  # Scissors
            elif their_choice == 3:  # Scissors
                my_choice = 1  # Rock
            total_score_of_game += my_choice
        elif expected_outcome == 0:
            my_choice = 0
            if their_choice == 1:  # Rock
                my_choice = 3  # Scissors
            elif their_choice == 2:  # Paper
                my_choice = 1  # Rock
            elif their_choice == 3:  # Scissors
                my_choice = 2  # Paper
            total_score_of_game += my_choice

        total_score_of_game += expected_outcome

    return total_score_of_game


def from_letter_to_expected_outcome(letter: str) -> int:
    if letter == "X":
        return 0
    elif letter == "Y":
        return 3
    elif letter == "Z":
        return 6


def from_letter_to_score_of_move(letter: str) -> int:
    return ord(letter) - ord("A") + 1
