# https://github.com/kenan238/aoc-2023/blob/main/day1/main.py

import re

nums = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
with open('./input.txt', 'r') as f:
    data = f.readlines()

def calibrationValue(txt: list[str], pattern: str) -> int:
    digits: list[str] = [str(nums.index(digit)) if digit in nums else digit for digit in re.findall(pattern, txt)]
    return int(digits[0] + digits[-1])

print(f"Part 1: {sum([calibrationValue(line, r'\d') for line in data])}")
print(f"Part 2: {sum([calibrationValue(line, r'(?=(' + "|".join(nums) + "|\\d))") for line in data])}")

# no regular expressions solutions

# https://www.reddit.com/r/adventofcode/comments/1883ibu/comment/kbm8u8t/?utm_source=share&utm_medium=web2x&context=3

with open("input.txt") as f:
    data = f.read().strip()

def calibration(data):
    ls = data.split("\n")
    ns = [re.findall(r"\d", x) for x in ls]
    # print(ns)
    return sum(int(n[0] + n[-1]) for n in ns)

# Part 1
print(f"Part 1: {calibration(data)}")

# Part 2
data = (
    data.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)
# print(data)
print(f"Part 2: {calibration(data)}")