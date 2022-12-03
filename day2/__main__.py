#!/usr/bin/env python3

from .part1 import get_total_score as get_total_score_p1
from .part2 import get_total_score as get_total_score_p2


def get_input(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


if __name__ == '__main__':
    print("\n======================")

    filenames = {"TEST INPUT": "day2/test_input.txt", "REAL INPUT": "day2/input.txt"}
    result_part1 = []
    result_part2 = []

    for type_of_input, filename in filenames.items():
        content = get_input(filename)

        total_score_of_part1 = get_total_score_p1(content)
        total_score_of_part2 = get_total_score_p2(content)

        result_part1.append(total_score_of_part1)
        result_part2.append(total_score_of_part2)

        print(f"\n{type_of_input}\n")
        print(f"--> Part 1: Total Score according to Strategy Guide: {total_score_of_part1}.")
        print(f"--> Part 2: Total Score according to Strategy Guide: {total_score_of_part2}.")

    assert result_part1[0] == 15
    assert result_part1[1] == 12458

    assert result_part2[0] == 12

    print("\n======================\n")
