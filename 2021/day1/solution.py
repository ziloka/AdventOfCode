#! /usr/bin/env python3
# https://www.reddit.com/r/adventofcode/comments/r66vow/comment/hmu09qs/?utm_source=share&utm_medium=web2x&context=3
import sys

def part1(lst: list) -> int:
    res = [ind + 1 for ind, x in enumerate(lst) if ind + 1 < len(lst) and lst[ind + 1] > x]
    return len(res)


def part2(lst: list) -> int:
    groups = [x + lst[ind + 1] + lst[ind + 2] for ind, x in enumerate(lst) if ind + 2 < len(lst)]
    return part1(groups)


def get_data(path):
    with open(path) as f:
        return [int(x) for x in f.readlines()]


if __name__ == '__main__':
    lines = get_data("./input.txt")

    r1 = part1(lines)
    r2 = part2(lines)

    print(f'part 1: {r1}')
    print(f'part 2: {r2}')