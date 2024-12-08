# https://github.com/danielhuang/aoc-2024/blob/master/src/bin/7.rs
import time
import re

def concat(a: int, b: int) -> int:
    return a * (10 ** (len(str(b)))) + b

def is_possible(goal: int, start: int, rest: list[int], part2: bool) -> bool:
    if not rest:
        return goal == start
    if start > goal:
        return False

    return (
        (part2 and is_possible(goal, concat(start, rest[0]), rest[1:], part2))
        or is_possible(goal, start * rest[0], rest[1:], part2)
        or is_possible(goal, start + rest[0], rest[1:], part2)
    )

input_data = open("input.txt").read()
for part2 in [False, True]:
    start_time = time.time()
    count = 0
    for line in input_data.splitlines():
        ints = list(map(int, re.split(r':?\s', line.strip())))
        goal = ints[0]
        others = ints[1:]
        if is_possible(goal, others[0], others[1:], part2):
            count += goal
    print(count)
    print(f"took {time.time() - start_time:.2f}s")
