#!/usr/bin/env python3


def get_total_score(strategy_guide: str) -> int:
    total_score_of_game = 0
    score_for_win = 6
    score_for_draw = 3

    for line in strategy_guide.splitlines():
        their_choice, my_choice = list(map(from_letter_to_score_of_move, line.split()))

        total_score_of_game += my_choice

        if is_draw(their_choice, my_choice):
            total_score_of_game += score_for_draw
        elif is_win(their_choice, my_choice):
            total_score_of_game += score_for_win

    return total_score_of_game


def from_letter_to_score_of_move(letter: str) -> int:
    character_code_for_capital_c = 67
    offset_base = "A" if ord(letter) <= character_code_for_capital_c else "X"
    return ord(letter) - ord(offset_base) + 1


def is_win(their_choice: int, my_choice: int) -> bool:
    return their_choice == my_choice - 1 or their_choice == my_choice + 2


def is_draw(their_choice: int, my_choice: int) -> bool:
    return their_choice == my_choice


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
