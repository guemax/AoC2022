#!/usr/bin/env python3


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

        result_part1.append()
        result_part2.append()

        print(f"\n{type_of_input}\n")
        print(f"--> Part 1: .")
        print(f"--> Part 2: .")

    print("\n======================\n")
