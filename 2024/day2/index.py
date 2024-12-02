from enum import Enum

class Direction(Enum):
    INCREASING = 1
    DECREASING = 2

def isGoodLevel(currLevel, prevLevel, direction):
    increasing = direction == Direction.DECREASING and currLevel < prevLevel
    decreasing = direction == Direction.INCREASING and currLevel > prevLevel

    differ = abs(currLevel - prevLevel)
    adjacent = differ >= 1 and differ <= 3
    
    return (increasing or decreasing) and adjacent

def determineDirection(currLevel, prevLevel):
    if currLevel > prevLevel:
        return Direction.INCREASING
    elif currLevel < prevLevel:
        return Direction.DECREASING

def isReportSafe(levels, problemDamperEnabled = False, count = 0):

    direction = None
    for i in range(1, len(levels)):
        if i == 1:
            if levels[i] > levels[i - 1]:
                direction = Direction.INCREASING
            elif levels[i] < levels[i - 1]:
                direction = Direction.DECREASING
        
        if not isGoodLevel(levels[i], levels[i - 1], direction):
            if problemDamperEnabled and count < 1:
                for j in range(0, len(levels)-1):
                    
                    testCurr = levels[j + 1]
                    testPrev = levels[0 if j == 0 else j - 1]
                    newReport = levels[:j] + levels[j + 1:]

                    if isGoodLevel(testCurr, testPrev, direction) and isReportSafe(newReport, problemDamperEnabled, count + 1):
                        return True
            break
            
        if i == len(levels) - 1:
            return True
        
    return False

reports = open("input.txt").read().splitlines()

parse = lambda report: [*map(int, report.split(" "))]

safe = 0
for report in reports:
    if isReportSafe(parse(report), problemDamperEnabled=False):
        safe += 1

print(f"part 1: {safe}")

print(f"10 1 3 5 8, {isReportSafe(parse('10 1 3 5 8'), True)}")

safe = 0
track = []
for report in reports:
    if isReportSafe(parse(report), problemDamperEnabled=True):
        safe += 1

# 277 too low
# 321 is wrong
print(f"part 2: {safe}")

# print("\n".join(track))

# for report in track:
#     print(f"{report}, {isReportSafe(parse(report), True)}")