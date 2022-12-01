#!/usr/bin/env python3

import unittest

from .__main__ import main


class TestDay1(unittest.TestCase):
    def setUp(self) -> None:
        super(TestDay1, self).setUp()

    def test_day_one(self) -> None:
        result = main("day1/test_input.txt")
        self.assertEqual(result, 24000)


if __name__ == '__main__':  # prame: no cover
    unittest.main()
