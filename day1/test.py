#!/usr/bin/env python3

import unittest

from .__main__ import get_max_total_calories, get_max_total_calories_of_top_three


class TestDay1(unittest.TestCase):
    def setUp(self) -> None:
        super(TestDay1, self).setUp()

    def test_day1_part1(self) -> None:
        result = get_max_total_calories("day1/test_input.txt")
        self.assertEqual(result, 24000)

    def test_day_1_part2(self) -> None:
        result = get_max_total_calories_of_top_three("day1/test_input.txt")
        self.assertEqual(result, 45000)


if __name__ == '__main__':  # prame: no cover
    unittest.main()
