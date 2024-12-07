from enum import Enum

class Direction(Enum):
    INCREASING = 1
    DECREASING = 2

def isGoodLevel(currLevel, prevLevel, direction):
    increasing = direction == Direction.INCREASING and currLevel > prevLevel
    decreasing = direction == Direction.DECREASING and currLevel < prevLevel

    differ = abs(currLevel - prevLevel)
    adjacent = 1 <= differ <= 3
    
    return (increasing or decreasing) and adjacent

def determineDirection(currLevel, prevLevel):
    if currLevel > prevLevel:
        return Direction.INCREASING
    elif currLevel < prevLevel:
        return Direction.DECREASING
    return None  # Explicitly return None if no direction can be determined

def isReportSafe(levels, problemDamperEnabled=False, count=0):
    direction = None
    for i in range(1, len(levels)):
        currLevel = levels[i]
        prevLevel = levels[i - 1]

        if i == 1:
            direction = determineDirection(currLevel, prevLevel)
            if direction is None:  # Skip to the next level if direction cannot be determined
                continue

        if (direction is None and i == 0) or not isGoodLevel(currLevel, prevLevel, direction):
            if problemDamperEnabled and count < 1:
                for j in range(len(levels)):
                    newReport = levels[:j] + levels[j + 1:]
                    if isReportSafe(newReport, problemDamperEnabled, count + 1):
                        return True
            return False
        
        if i == len(levels) - 1:
            return True
        
    return False

reports = open("input.txt").read().splitlines()

parse = lambda report: [*map(int, report.split(" "))]

# Part 1
safe = 0
for report in reports:
    if isReportSafe(parse(report), problemDamperEnabled=False):
        safe += 1

print(f"part 1: {safe}")

# Part 2
safe = 0
diff2 = open("diff2.txt", "w")
for report in reports:
    if isReportSafe(parse(report), problemDamperEnabled=True):
        safe += 1
    else:
        diff2.write(report + "\n")

print(f"part 2: {safe}")