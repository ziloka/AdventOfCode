import math

with open('./input.txt', 'r') as f:
    data = f.readlines()

maxColorTable = { "red": 12, "green": 13, "blue": 14 }
sumOfIds = 0
sumOfpowers = 0
for (i, line) in enumerate(data):
    gameId = i + 1
    sets = [gameSet.split(", ") for gameSet in line.strip().split(": ")[1].split("; ")]
    cubes = [cube.split(" ") for bag in sets for cube in bag]
  
    minColorTable = { "red": 0, "green": 0, "blue": 0 }

    valid = True
    for cube in cubes:
        amount = int(cube[0])
        color = cube[1]
        # part 1
        if amount > maxColorTable[color]:
            valid = False
        
        # part 2
        if amount > minColorTable[color]:
            minColorTable[color] = amount
    if valid:
        sumOfIds += gameId
    sumOfpowers += math.prod(minColorTable.values())


print(f"part 1: {sumOfIds}")
print(f"part 2: {sumOfpowers}")