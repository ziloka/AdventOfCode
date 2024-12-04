import itertools

input = open("input.txt", "r").read().split("\n")
matrix = [list(line) for line in input]

counter = 0
positions = []
for i in range(1, len(matrix)-2):
    substr = [
        [matrix[i-1][-1], matrix[i][i], matrix[i+1][i+1], matrix[i+2][i+2]], # \
        [matrix[i-1][i-1], matrix[i][i], matrix[i-1][i+1], matrix[i-2][i+2]], # /
        [matrix[i][i-1], matrix[i][i], matrix[i][i+1], matrix[i][i+2]], # -
        [matrix[i-1][i], matrix[i][i], matrix[i][i+1], matrix[i][i+2]] # |
    ]
    xmas = list(itertools.chain.from_iterable([["".join(s), "".join(s[::-1])] for s in substr]))

    if any([s == "XMAS" for s in xmas]):
        counter += 1
print(f"part 1: {counter}")