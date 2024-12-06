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
        self.matrix = []
        self.visual = []
        rows = open(filename).read().split("\n")
        for i, row in enumerate(rows):
            elements = list(row)
            for j, e in enumerate(elements):
                if e in [e.value for e in GUARD]: 
                    self.guard_pos = [i, j] 
            self.matrix.append(elements)
            self.visual.append(elements.copy())

    def debug(self, table):
        for line in table:
            print("".join(line))
        print()

    def is_valid_pos(self, coords):
        return 0 <= coords[0] < len(self.matrix) and 0 <= coords[1] < len(self.matrix[0])

    def get_element(self, coords):
        if not self.is_valid_pos(coords):
            return None
        return self.matrix[coords[0]][coords[1]]
    
    def set_element(self, coords, value):
        self.matrix[coords[0]][coords[1]] = value

    def set_visual_element(self, coords, value):
        self.visual[coords[0]][coords[1]] = value

    def execute_protocol(self):
        positions = []
        guard = self.get_element(self.guard_pos)
        if guard == GUARD.UP.value and self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[0] -= 1
                positions.append(self.guard_pos.copy())
                if not self.is_valid_pos(self.guard_pos):
                    return None
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.UP.value
        elif guard == GUARD.DOWN.value and self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[0] += 1
                positions.append(self.guard_pos.copy())
                if not self.is_valid_pos(self.guard_pos):
                    return None
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.DOWN.value
        elif guard == GUARD.LEFT.value and self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[1] -= 1
                positions.append(self.guard_pos.copy())
                if not self.is_valid_pos(self.guard_pos):
                    return None
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.LEFT.value
        elif guard == GUARD.RIGHT.value and self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[1] += 1
                positions.append(self.guard_pos.copy())
                if not self.is_valid_pos(self.guard_pos):
                    return None
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.RIGHT.value

        # guard in front of obstruction
        match guard:
            case GUARD.LEFT.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.UP.value
            case GUARD.UP.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.RIGHT.value
            case GUARD.RIGHT.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.DOWN.value
            case GUARD.DOWN.value:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.LEFT.value
            case _:
                raise Exception("invalid guard")
        return positions
        
    def part1(self):
        while True:
            positions = self.execute_protocol()
            if positions == None:
                break
        
        count = 0
        for line in self.visual:
            for element in line:
                if element == "X":
                    count += 1
        return count
        # distinct_positions = set()
        # while True:
        #     positions = self.execute_protocol()
        #     if positions == None:
        #         break
        #     # print(positions)
        #     for pos in positions:
        #         distinct_positions.add(f"{pos[0]}_{pos[1]}")
        # # self.debug(self.visual)
        # return len(distinct_positions)

map = Map("input.txt")
# map.debug()
print(f"part 1: {map.part1()}")
# print(matrix)