#!/usr/bin/env python3


def get_max_total_calories(file: str):
    max_calories = 0
    current_calories = 0

    with open(file, "r") as f:
        content = f.read()

    for line in content.splitlines():
        if line == "":
            max_calories = max(current_calories, max_calories)
            current_calories = 0
            continue

        current_calories += int(line)

    return max_calories


if __name__ == '__main__':
    test_input = "day1/test_input.txt"
    input_ = "day1/input.txt"

    print("\n===== TEST INPUT =====")
    solution = get_max_total_calories(test_input)
    print(f"The Elf with the most Calories is carrying {solution} Calories.")
