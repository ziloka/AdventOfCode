import inspect
from enum import Enum

# https://stackoverflow.com/a/19300424
class GUARD(Enum):
    def __new__(cls, *args, **kwds):
          value = len(cls.__members__) + 1
          obj = object.__new__(cls)
          obj._value_ = value
          return obj
    def __init__(self, a, b):
        self.num = a
        self.char = b

    UP = 1, "^",
    RIGHT = 2, ">",
    DOWN = 3, "v"
    LEFT = 4, "<"

class OBJECT(Enum):
    OBSTRUCTION = "#"
    EMPTY = "."

class Map():
    def __init__(self, filename="example.txt"):
        self.init(filename)
    
    def init(self, filename):
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
        if guard == GUARD.UP.char and self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[0] -= 1
                if not self.is_valid_pos(self.guard_pos):
                    return [*positions, None]
                positions.append(self.guard_pos.copy())
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.UP.char
        elif guard == GUARD.DOWN.char and self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[0] += 1
                if not self.is_valid_pos(self.guard_pos):
                    return [*positions, None]
                positions.append(self.guard_pos.copy())
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.DOWN.char
        elif guard == GUARD.LEFT.char and self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[1] -= 1
                if not self.is_valid_pos(self.guard_pos):
                    return [*positions, None]
                positions.append(self.guard_pos.copy())
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.LEFT.char
        elif guard == GUARD.RIGHT.char and self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[1] += 1
                if not self.is_valid_pos(self.guard_pos):
                    return [*positions, None]
                positions.append(self.guard_pos.copy())
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.RIGHT.char

        # guard in front of obstruction
        match guard:
            case GUARD.LEFT.char:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.UP.char
            case GUARD.UP.char:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.RIGHT.char
            case GUARD.RIGHT.char:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.DOWN.char
            case GUARD.DOWN.char:
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.LEFT.char
            case _:
                raise Exception("invalid guard")
        return positions
        
    def part1(self):
        debug_positions = []
        distinct_positions = set()
        # https://stackoverflow.com/a/654002
        while True:
            positions = self.execute_protocol()
            for pos in positions:
                if pos == None:
                    break
                if f"{pos[0]}_{pos[1]}" not in distinct_positions:
                    debug_positions.append(pos)
                distinct_positions.add(f"{pos[0]}_{pos[1]}")
            else:
                continue
            break
    
        return len(distinct_positions)

    def inf_loops(self, positions):
        # if guard goes on the same path twice, it is an inf loop
        # if guard makes three direction turns, try placing an obstruction to create inf loop
        POSSIBLITIES = [
            [GUARD.UP.value, GUARD.LEFT.value, GUARD.RIGHT.value],
            [GUARD.LEFT.value, GUARD.RIGHT.value],
            [GUARD.UP.value, GUARD.LEFT.value],
            [GUARD.DOWN.value, GUARD.RIGHT.value]
        ]
        
        pass

    def part2(self):
        self.init()


map = Map("input.txt")
# map.debug()
print(GUARD.UP.char)
print(f"part 1: {map.part1()}")
# print(matrix)