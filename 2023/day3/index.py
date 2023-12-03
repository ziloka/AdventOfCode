with open("input.txt") as file:
    data = file.readlines()

table = [[*line.strip()] for line in data]
isSymbol = lambda s: s != "." and not s.isdigit()

partNumbersSum = 0
rowIndex = 0
while rowIndex < len(table):
    row = table[rowIndex]
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
            if num == 2:
                print(f"[{num}] row: {rowIndex} col: {columnIndex} end: {end}")
            # check if there is symbol adjacent to number (including diagonally)
            valid = False
            for i in range(columnIndex, end):
                if i == columnIndex: # check top left diagonal, left side, and bottom left diagonal
                    # check if there is anything to even check
                    if i == len(table):
                        continue
                    if num == 2:
                        print(f"gets here col: {i} end: {end-1}")
                    if rowIndex == 0:
                        if isSymbol(table[rowIndex][i-1]) or isSymbol(table[rowIndex+1][i-1]): # only check for left side and bottom left diagonal
                            valid = True
                            break
                    elif rowIndex == len(table)-1:
                        if isSymbol(table[rowIndex][i-1]) or isSymbol(table[rowIndex-1][i-1]): # check left side, and top left diagonal
                            valid = True
                            break
                    else:
                        if isSymbol(table[rowIndex][i-1]) or isSymbol(table[rowIndex-1][i-1]) or isSymbol(table[rowIndex+1][i-1]): # check left side, top left diagonal and bottom left diagonal
                            valid = True
                            break
                if i == end-1: # check top right diagonal, right side, and top right diagonal
                    # check if there is anything to even check 
                    if i == len(table[0])-1:
                        continue
                    if rowIndex == 0:
                        if isSymbol(table[rowIndex][i+1]) or isSymbol(table[rowIndex+1][i+1]): # only check for right side and bottom right diagonal
                            valid = True
                            break
                    elif rowIndex == len(table)-1:
                        if isSymbol(table[rowIndex][i+1]) or isSymbol(table[rowIndex-1][i+1]): # check right side, and top right diagonal
                            valid = True
                            break
                    else: # check right side, top right diagonal and bottom right diagonal
                        if isSymbol(table[rowIndex][i+1]) or isSymbol(table[rowIndex+1][i+1]) or isSymbol(table[rowIndex-1][i+1]):
                            valid = True
                            break
                # check top, bottom, of character
                if rowIndex == 0: # only check bottom side
                    if isSymbol(table[rowIndex+1][i]):
                        valid = True
                        break
                elif rowIndex == len(table)-1: # only check top side
                    if isSymbol(table[rowIndex-1][i]):
                        valid = True
                        break
                else: # check top and bottom
                    if isSymbol(table[rowIndex-1][i]) or isSymbol(table[rowIndex+1][i]):
                        valid = True
                        break
            if valid:
                partNumbersSum += num
            # else:
                # print(f"invalid {num}")
            columnIndex = end
        else:
            columnIndex += 1
    rowIndex += 1

# edge case .2=
print(f"part 1: {partNumbersSum}")
# 530477 is too low