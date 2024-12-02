leftList = []
rightList = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        leftElement, rightElement = line.strip().split(" " * 3)
        leftList.append(int(leftElement))
        rightList.append(int(rightElement))

leftList.sort()
rightList.sort()

pairs = []
for i in range(len(leftList)):
    pairs.append((leftList[i], rightList[i]))

print(f"part 1: {sum(map(lambda pair: abs(pair[0] - pair[1]), pairs))}")

for i in range(len(leftList)):
    leftValue = leftList[i]
    counts = 0
    for rightValue in rightList:
        if leftValue == rightValue:
            counts += 1
    leftList[i] *= counts

print(f"part 2: {sum(leftList)}")