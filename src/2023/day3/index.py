with open("input.txt") as file:
    data = file.readlines()

table = [[*line.strip()] for line in data]

# check if there is symbol adjacent to number (including diagonally)
def findSymbol(rowIndex, columnIndex, end, isSymbol, exclude=[]) -> (int, int):
    valid = (-1, -1)
    for i in range(columnIndex, end):
        if i == columnIndex: # start of number
            if i == len(table):
                continue
            if rowIndex == 0:
                if i-1 >= 0 and not (rowIndex, i-1) in exclude and isSymbol(table[rowIndex][i-1]): # left side
                    valid = (rowIndex, i-1)
                    break
                elif rowIndex+1 < len(table) and i-1 >= 0 and not (rowIndex+1, i-1) in exclude and isSymbol(table[rowIndex+1][i-1]): # bottom left diagonal
                    valid = (rowIndex+1, i-1)
                    break
            elif rowIndex == len(table)-1:
                if i-1 >= 0 and not (rowIndex, i-1) in exclude and isSymbol(table[rowIndex][i-1]): # left side
                    valid = (rowIndex, i-1)
                    break
                if rowIndex-1 >= 0 and i-1 >= 0 and not (rowIndex-1, i-1) in exclude and isSymbol(table[rowIndex-1][i-1]): # top left diagonal
                    valid = (rowIndex-1, i-1)
                    break
            else:
                if i-1 >= 0 and not (rowIndex, i-1) in exclude and isSymbol(table[rowIndex][i-1]): # left side
                    valid = (rowIndex, i-1)
                    break
                elif rowIndex-1 >= 0 and i-1 >= 0 and not (rowIndex-1, i-1) in exclude and isSymbol(table[rowIndex-1][i-1]): # top left diagonal
                    valid = (rowIndex-1, i-1)
                    break
                elif rowIndex+1 < len(table) and i-1 >= 0 and not (rowIndex+1, i-1) in exclude and isSymbol(table[rowIndex+1][i-1]): # bottom left diagonal
                    valid = (rowIndex+1, i-1)
                    break
        if i == end-1: # end of number
            if i == len(table[0])-1:
                continue
            if rowIndex == 0:
                if i+1 < len(table[0]) and not (rowIndex, i+1) in exclude and isSymbol(table[rowIndex][i+1]): # check for right side
                    valid = (rowIndex, i+1)
                    break
                elif rowIndex+1 < len(table) and i+1 < len(table[0]) and not (rowIndex+1, i+1) in exclude and isSymbol(table[rowIndex+1][i+1]): # bottom right diagonal
                    valid = (rowIndex+1, i+1)
                    break
            elif rowIndex == len(table)-1:
                if i+1 < len(table[0]) and not (rowIndex, i+1) in exclude and isSymbol(table[rowIndex][i+1]): # check right side
                    valid = (rowIndex, i+1)
                    break
                elif rowIndex-1 >= 0 and i+1 < len(table[0]) and not (rowIndex-1, i+1) in exclude and isSymbol(table[rowIndex-1][i+1]): # top right diagonal
                    valid = (rowIndex-1, i+1)
            else:
                if i+1 < len(table[0]) and not (rowIndex, i+1) in exclude and isSymbol(table[rowIndex][i+1]):# check right side
                    valid = (rowIndex, i+1)
                    break
                elif rowIndex+1 < len(table) and i+1 < len(table[0]) and not (rowIndex+1, i+1) in exclude and isSymbol(table[rowIndex+1][i+1]): # top right diagonal
                    valid = (rowIndex+1, i+1)
                    break
                elif rowIndex-1 >= 0 and i+1 < len(table[0]) and not (rowIndex-1, i+1) in exclude and isSymbol(table[rowIndex-1][i+1]): # bottom right diagonal
                    valid = (rowIndex-1, i+1)
                    break
        if rowIndex == 0: 
            if rowIndex+1 < len(table) and not (rowIndex+1, i) in exclude and isSymbol(table[rowIndex+1][i]): # bottom
                valid = (rowIndex+1, i)
                break
        elif rowIndex == len(table)-1:
            if rowIndex-1 >= 0 and not (rowIndex-1, i) in exclude and isSymbol(table[rowIndex-1][i]): # top
                valid = (rowIndex-1, i)
                break
        else:
            if rowIndex-1 >= 0 and not (rowIndex-1, i) in exclude and isSymbol(table[rowIndex-1][i]): # top
                valid = (rowIndex-1, i)
                break
            elif rowIndex+1 < len(table) and not (rowIndex+1, i) in exclude and isSymbol(table[rowIndex+1][i]): # bottom
                valid = (rowIndex+1, i)
                break
    return valid

partNumbersSum = 0
rowIndex = 0
foundGears = []
gearRatioSum = 0
while rowIndex < len(table):
    columnIndex = 0
    while columnIndex < len(table[rowIndex]):
        ch = table[rowIndex][columnIndex]
        # the meaty part starts here
        if ch.isdigit():
            end = columnIndex
            while end < len(table[rowIndex]):
                if not table[rowIndex][end].isdigit():
                    break
                end += 1
            num = int("".join(table[rowIndex][columnIndex:end]))
            # part 1
            symbolLocation = findSymbol(rowIndex, columnIndex, end, lambda c: c != "." and not c.isdigit())
            if symbolLocation != (-1, -1):
                partNumbersSum += num
            # part 2
            if table[symbolLocation[0]][symbolLocation[1]] == "*":
                exclude = [(rowIndex, col) for col in range(columnIndex, end)]
                if symbolLocation == (-1, -1):
                    exclude.append(symbolLocation)
                numberLocation = findSymbol(symbolLocation[0], symbolLocation[1], symbolLocation[1]+1, lambda n: n.isdigit(), exclude)
                if numberLocation != (-1, -1):
                    num2End = numberLocation[1]
                    while num2End < len(table[numberLocation[0]]):
                        if not table[numberLocation[0]][num2End].isdigit():
                            break
                        num2End += 1
                    start = numberLocation[1]
                    while start >= 0:
                        if not table[numberLocation[0]][start].isdigit():
                            break
                        start -= 1
                    start += 1
                    num2 = int("".join(table[numberLocation[0]][start:num2End]))
                    if (rowIndex, columnIndex) != (numberLocation[0], start) and not [(rowIndex, columnIndex), (numberLocation[0], start)] in foundGears and not [(numberLocation[0], start), (rowIndex, columnIndex)] in foundGears:
                        foundGears.append([(rowIndex, columnIndex), (numberLocation[0], start)])
                        gearRatio = num * num2
                        gearRatioSum += gearRatio       
            columnIndex = end
        else:
            columnIndex += 1
    rowIndex += 1

# edge case .2=
print(f"part 1: {partNumbersSum}")
# 81338178 answer too high
# 80253814
# 701 127
print(f"part 2: {gearRatioSum}")