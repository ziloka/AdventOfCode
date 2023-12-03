#!/usr/bin/python3

# part 1 is not 33010101016442

import re
import math
import functools
import unittest

arr = open("input.txt").read().rstrip().split("\n")
BASE = 5

# basically base 5 num to base 10 with extra steps
def SNAFU_to_decimal(str):
    decimal_number = 0
    for i in range(0, len(str)):
        digit = str[i]
        match digit:
            case "=":
                digit = -2
            case "-":
                digit = -1
            case _: # 0, 1, 2
                digit = int(digit)
        place_value = BASE ** (len(str)-i-1)
        decimal_number += digit * place_value
    return decimal_number

regex = re.compile(r"^0+", re.IGNORECASE)
def decimal_to_SNAFU(num):
    string = ""
    index = math.ceil(math.log(num, BASE))
    while index >= 0:
        place_value = 5 ** index
        # find number that will make decimal number closest to zero
        # https://stackoverflow.com/a/12141207
        digit = min([-2, -1, 0, 1, 2], key=lambda n: abs((n * place_value)-num))
        num -= digit * place_value
        match digit:
            case -2:
                digit = "="
            case -1:
                digit = "-"
            case _:
                digit = str(digit)
        string += digit 
        index -= 1
    return re.sub("^0+", "", string)

# python -m unittest main.py
class SNAFU2DECIMAL(unittest.TestCase):

    def test_one(self):
        self.assertEqual(decimal_to_SNAFU(1), "1")

    def test_two(self):
        self.assertEqual(decimal_to_SNAFU(2), "2")

    def test_three(self):
        self.assertEqual(decimal_to_SNAFU(3), "1=")

    def test_four(self):
        self.assertEqual(decimal_to_SNAFU(4), "1-")

    def test_five(self):
        self.assertEqual(decimal_to_SNAFU(5), "10")

    def test_six(self):
        self.assertEqual(decimal_to_SNAFU(6), "11")

    def test_seven(self):
        self.assertEqual(decimal_to_SNAFU(7), "12")

    def test_eight(self):
        self.assertEqual(decimal_to_SNAFU(8), "2=")

    def test_nine(self):
        self.assertEqual(decimal_to_SNAFU(9), "2-")

    def test_ten(self):
        self.assertEqual(decimal_to_SNAFU(10), "20")

    def test_fifteen(self):
        self.assertEqual(decimal_to_SNAFU(15), "1=0")

    def test_twenty(self):
        self.assertEqual(decimal_to_SNAFU(20), "1-0")

    def test_two_thousand_twenty_two(self):
        self.assertEqual(decimal_to_SNAFU(2022), "1=11-2")

    def test_twelve_thousand_three_hundred_forty_five(self):
        self.assertEqual(decimal_to_SNAFU(12345), "1-0---0")

    def test_two_hundred_two_million_two_hundred_twelve_thousand_three_hundred_forty_five(self):
        self.assertEqual(decimal_to_SNAFU(314159265), "1121-1110-1=0")

class SNAFU2DECIMAL(unittest.TestCase):

    def test_one(self):
        self.assertEqual(SNAFU_to_decimal("1=-0-2"), 1747)

    def test_two(self):
        self.assertEqual(SNAFU_to_decimal("12111"), 906)

    def test_three(self):
        self.assertEqual(SNAFU_to_decimal("2=0="), 198)

    def test_four(self):
        self.assertEqual(SNAFU_to_decimal("21"), 11)

    def test_five(self):
        self.assertEqual(SNAFU_to_decimal("2=01"), 201)

    def test_six(self):
        self.assertEqual(SNAFU_to_decimal("111"), 31)

    def test_seven(self):
        self.assertEqual(SNAFU_to_decimal("20012"), 1257)

    def test_eight(self):
        self.assertEqual(SNAFU_to_decimal("112"), 32)

    def test_nine(self):
        self.assertEqual(SNAFU_to_decimal("1=-1="), 353)

    def test_ten(self):
        self.assertEqual(SNAFU_to_decimal("1-12"), 107)

    def test_eleven(self):
        self.assertEqual(SNAFU_to_decimal("12"), 7)

    def test_twelve(self):
        self.assertEqual(SNAFU_to_decimal("1="), 3)

    def test_thirteen(self):
        self.assertEqual(SNAFU_to_decimal("122"), 37)

# print(SNAFU_to_decimal("2=-01")) # 976
# print(SNAFU_to_decimal("1=11-2")) # 2022
# print(decimal_to_SNAFU("9")) # 2-
# print(decimal_to_SNAFU(20)) # 1-0
# print(decimal_to_SNAFU(314159265)) # 1121-1110-1=0

print(functools.reduce(lambda a, b: a + b, list(map(SNAFU_to_decimal, arr))))

# if __name__ == '__main__':
#     unittest.main()
