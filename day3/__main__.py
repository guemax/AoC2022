#!/usr/bin/env python3


def get_sum_of_priorities(content_of_rucksacks: str) -> int:
    total_priorities = 0

    for rucksack in content_of_rucksacks.splitlines():
        size_of_compartment = int(len(rucksack) / 2)
        intersecting_letter = ''.join(set(rucksack[:size_of_compartment]) & set(rucksack[size_of_compartment:]))

        current_priority = ord(intersecting_letter.lower()) - ord("a") + 1
        if intersecting_letter.isupper():
            current_priority += 26

        total_priorities += current_priority

    return total_priorities


def get_input(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


if __name__ == '__main__':
    print("\n======================")

    filenames = {"TEST INPUT": "day3/test_input.txt", "REAL INPUT": "day3/input.txt"}
    result_part1 = []
    result_part2 = []

    for type_of_input, filename in filenames.items():
        content = get_input(filename)
        sum_of_priorities = get_sum_of_priorities(content)

        result_part1.append(sum_of_priorities)

        print(f"\n{type_of_input}\n")
        print(f"--> Part 1: The sum of the priorities the items is {sum_of_priorities}.")
        print(f"--> Part 2: .")

    assert result_part1[0] == 157
    assert result_part1[1] == 8039

    print("\n======================\n")
