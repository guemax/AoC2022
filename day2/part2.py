#!/usr/bin/env python3


def get_total_score(strategy_guide: str) -> int:
    total_score_of_game = 0

    for line in strategy_guide.splitlines():
        their_choice, expected_outcome = list(map(from_letter_to_value, line.split(" ")))
        my_choice = 0

        if expected_outcome == 3:
            my_choice = their_choice
        elif expected_outcome == 6:
            my_choice = their_choice + 1 if their_choice != 3 else 1
        elif expected_outcome == 0:
            my_choice = their_choice - 1 if their_choice != 1 else 3

        total_score_of_game += my_choice + expected_outcome

    return total_score_of_game


def from_letter_to_value(letter: str) -> int:
    if is_their_move(letter):
        return ord(letter) - ord("A") + 1
    else:  # Is the expected outcome of this round
        return (ord(letter) - ord("X")) * 3


def is_their_move(letter: str) -> bool:
    return ord(letter) <= 67  # ord("C")

