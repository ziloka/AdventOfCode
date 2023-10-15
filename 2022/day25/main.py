"""AOC Day 25"""

import re
import math
import functools

arr = open("input.txt", encoding="UTF-8").read().rstrip().split("\n")
SNAFU_BASE = 5

# basically base 5 num to base 10 with extra steps
def snafu2decimal(snafu):
    """Converts the SNAFU number to base 10"""
    decimal_number = 0
    for (i, digit) in enumerate(snafu):
        match digit:
            case "=":
                digit = -2
            case "-":
                digit = -1
            case _: # 0, 1, 2
                digit = int(digit)
        place_value = SNAFU_BASE ** (len(snafu)-i-1)
        decimal_number += digit * place_value
    return decimal_number

regex = re.compile(r"^0+", re.IGNORECASE)
def decimal2snafu(num):
    """Converts the base 10 number to SNAFU"""
    string = ""
    index = math.ceil(math.log(num, SNAFU_BASE))
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

print(f"part 1: {decimal2snafu(functools.reduce(lambda a, b: a + b, list(map(snafu2decimal, arr))))}")

# if __name__ == '__main__':
#     unittest.main()
