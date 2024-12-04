input = open("input.txt", "r").read().split("\n")
matrix = [list(line) for line in input]

def part1():
    counter = 0
    # debug = [["."] * len(line) for line in input]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            candidates = [
                [[i-1,j-1], [i,j], [i+1,j+1], [i+2,j+2]], # \
                [[i+1,j-1], [i,j], [i-1,j+1], [i-2,j+2]], # /
                [[i,j-1], [i,j], [i,j+1], [i,j+2]], # -
                [[i-1,j], [i,j], [i+1,j], [i+2,j]] # |
            ]

            # determine what candidates are invalid, all positions should be valid positions in matrix
            candidates = [candidate for candidate in candidates if all([0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0]) for pos in candidate])]

            for candidate in candidates:
                string = "".join(map(lambda s: matrix[s[0]][s[1]], candidate))
                if string == "XMAS" or string[::-1] == "XMAS":

                    # for debugging purposes
                    # for pos in candidate:
                    #     debug[pos[0]][pos[1]] = matrix[pos[0]][pos[1]]
                    counter += 1
    # print("\n".join(list(map(lambda s: "".join(s), debug))))
    return counter

print(f"part 1: {part1()}")

def part2():
    counter = 0
    # debug = [["."] * len(line) for line in input]
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            if matrix[i][j] != "A":
                continue

            candidate = [
                [[i-1,j-1], [i,j], [i+1,j+1]], # \
                [[i+1,j-1], [i,j], [i-1,j+1]], # /
            ]

            left_diagonal = "".join(map(lambda s: matrix[s[0]][s[1]], candidate[0]))
            right_diagonal = "".join(map(lambda s: matrix[s[0]][s[1]], candidate[1]))

            if (left_diagonal == "MAS" and right_diagonal == "MAS" or
                left_diagonal == "MAS" and right_diagonal[::-1] == "MAS" or
                left_diagonal[::-1] == "MAS" and right_diagonal == "MAS" or
                left_diagonal[::-1] == "MAS" and right_diagonal[::-1] == "MAS"):

                counter += 1
                # for debugging purposes
                # for word_pos in candidate:
                #     for pos in word_pos:
                #         debug[pos[0]][pos[1]] = matrix[pos[0]][pos[1]]
    return counter
            
# print("\n".join(list(map(lambda s: "".join(s), debug))))
print(f"part 2: {part2()}")
