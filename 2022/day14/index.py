# paths = list(map(lambda s: s.split(","), open("input.txt", "r").read().rstrip().split(" -> ")))
input = open("input.txt", "r").read().rstrip()
paths = input.split("\n")

def printMatrix(matrix: list[list[list[str]]]):
    for row in matrix:
        for element in row:
            print(f"{element}", sep="")
        print()

rocks = list(map(lambda path: list(map(lambda line: list(map(int, line.split(","))), path)), list(map(lambda s: s.split(" -> "), paths))))

rock = "#"
air = "."
source_sand = "+"
rest_sand = "o"

flatten = [rock for path in rocks for line in path for rock in line]

x_values = flatten[::2]
y_values = flatten[1::2]

# find farthest x value from 500 (for values smaller than 500 (left side))
farthest_x_value_left = 500 - max(x_values, key=lambda n: 500 - n)
farthest_x_value_right = max(x_values, key=lambda n: n - 500) - 500

farthest_y_value = max(y_values)

matrix = [[air * (farthest_x_value_left + farthest_x_value_right + 1) ] * farthest_y_value]

# Put rock structures on empty matrix

printMatrix(matrix)

