#!/usr/bin/env python3


def get_sum_of_priorities(rucksacks: str) -> int:
    total_priorities = 0

    for rucksack in rucksacks.splitlines():
        size_of_compartment = int(len(rucksack) / 2)
        total_priorities += get_current_priority(
            set(rucksack[:size_of_compartment]) & set(rucksack[size_of_compartment:])
        )

    return total_priorities


def get_current_priority(intersecting_set: set) -> int:
    intersecting_letter = ''.join(intersecting_set)

    current_priority = ord(intersecting_letter.lower()) - ord("a") + 1
    if intersecting_letter.isupper():
        current_priority += 26

    return current_priority


def get_sum_of_priorities_part2(rucksacks: str) -> int:
    total_priorities = 0
    rucksacks_of_group = []
    i = 0

    for rucksack in rucksacks.splitlines():
        rucksacks_of_group.append(rucksack)
        i += 1

        if i == 3:
            total_priorities += get_current_priority(
                set(rucksacks_of_group[0]) & set(rucksacks_of_group[1]) & set(rucksacks_of_group[2])
            )
            rucksacks_of_group = []
            i = 0

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

        sum_of_priorities_p1 = get_sum_of_priorities(content)
        sum_of_priorities_p2 = get_sum_of_priorities_part2(content)

        result_part1.append(sum_of_priorities_p1)
        result_part2.append(sum_of_priorities_p2)

        print(f"\n{type_of_input}\n")
        print(f"--> Part 1: The sum of the priorities of all elves is {sum_of_priorities_p1}.")
        print(f"--> Part 2: The sum of the priorities of all groups is {sum_of_priorities_p2}.")

    assert result_part1[0] == 157
    assert result_part1[1] == 8039

    assert result_part2[0] == 70
    assert result_part2[1] == 2510

    print("\n======================\n")
