from enum import Enum

class GUARD(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

class OBJECT(Enum):
    OBSTRUCTION = "#"
    EMPTY = "."

class Map():
    def __init__(self, filename="example.txt"):
        matrix = []
        rows = open(filename).read().split("\n")
        for i, row in enumerate(rows):
            elements = list(row)
            for j, e in enumerate(elements):
                if e in [e.value for e in GUARD]: 
                    self.guard_pos = [i, j] 
            matrix.append(elements)
        self.matrix = matrix

    def debug(self):
        for line in self.matrix:
            print("".join(line))
        print()

    def get_element(self, coords):
        return self.matrix[coords[0]][coords[1]]
    
    def set_element(self, coords, value):
        self.matrix[coords[0]][coords[1]] = value

    def execute_protocol(self):
        guard = self.get_element(self.guard_pos)
        if guard == GUARD.LEFT.value and self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = OBJECT.EMPTY.value
                self.guard_pos[0] -= 1
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.LEFT.value
        elif guard == GUARD.RIGHT.value and self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = OBJECT.EMPTY.value
                self.guard_pos[0] += 1
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.RIGHT.value
        elif guard == GUARD.UP.value and self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = OBJECT.EMPTY.value
                self.guard_pos[1] -= 1
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.UP.value
        elif guard == GUARD.DOWN.value and self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = OBJECT.EMPTY.value
                self.guard_pos[1] += 1
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.DOWN.value
        # there is sitting in front of obstruction thing
        match guard:
            case GUARD.LEFT.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.DOWN.value
            case GUARD.RIGHT.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.UP.value
            case GUARD.UP.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.LEFT.value
            case GUARD.DOWN.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.RIGHT.value
            # case _:
                # print('what am i suppose to do now')
                # self.debug()
    def part1(self):
        distinct_positions = set()
        finished_complete_cycle = False
        while not finished_complete_cycle:
            self.execute_protocol()
            pos_str = f"{self.guard_pos[0]}_{self.guard_pos[1]}"
            if pos_str not in distinct_positions:
                distinct_positions.add(pos_str)
            print(len(distinct_positions))

map = Map()
# map.debug()
map.part1()
# print(matrix)