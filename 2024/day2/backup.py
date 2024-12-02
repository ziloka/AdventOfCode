from enum import Enum

class Direction(Enum):
    INCREASING = 1
    DECREASING = 2

def isReportSafe(report):
    levels = [*map(int, report.split(" "))]

    direction = None
    for i in range(1, len(levels)):
        if i == 1:
            if levels[i] > levels[i - 1]:
                direction = Direction.INCREASING
            elif levels[i] < levels[i - 1]:
                direction = Direction.DECREASING
        
        notIncreasing = direction == Direction.INCREASING and levels[i] < levels[i - 1]
        notDecreasing = direction == Direction.DECREASING and levels[i] > levels[i - 1]

        differ = abs(levels[i] - levels[i - 1])
        adjacent = differ >= 1 and differ <= 3

        if notIncreasing or notDecreasing or not adjacent:
            break

        if i == len(levels) - 1:
            return True

    return False

reports = open("input.txt").read().splitlines()

safe = 0
for report in reports:
    if isReportSafe(report, enableProblemDamper=False):
        safe += 1

print(f"part 1: {safe}")

safe = 0
for report in reports:
    if isReportSafe(report, enableProblemDamper=True):
        safe += 1

