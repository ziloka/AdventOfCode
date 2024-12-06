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
        if guard == GUARD.UP.value and self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[0] -= 1
                if not self.is_valid_pos(self.guard_pos):
                    return [*positions, None]
                positions.append(self.guard_pos.copy())
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.UP.value
        elif guard == GUARD.DOWN.value and self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[0] += 1
                if not self.is_valid_pos(self.guard_pos):
                    return [*positions, None]
                positions.append(self.guard_pos.copy())
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.DOWN.value
        elif guard == GUARD.LEFT.value and self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[1] -= 1
                if not self.is_valid_pos(self.guard_pos):
                    return [*positions, None]
                positions.append(self.guard_pos.copy())
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.LEFT.value
        elif guard == GUARD.RIGHT.value and self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.set_visual_element(self.guard_pos, "X")
                self.guard_pos[1] += 1
                if not self.is_valid_pos(self.guard_pos):
                    return [*positions, None]
                positions.append(self.guard_pos.copy())
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
    
    def create_infinite_loops(self):
        pass
        
    def part1(self):
        while True:
            positions = self.execute_protocol()
            if any([pos == None for pos in positions]):
                break
        
        original = open("expected.txt", "w")
        count = 0
        for i, line in enumerate(self.visual):
            for j, element in enumerate(line):
                if element == "X":
                    original.write(f"{i} {j}\n")
                    count += 1
        
        self.init("input.txt")

        new = open("actual.txt", "w")
        debug_positions = []
        distinct_positions = set()
        # https://stackoverflow.com/a/654002
        while True:
            positions = self.execute_protocol()
            # print(positions)
            for pos in positions:
                if pos == None:
                    break
                if f"{pos[0]}_{pos[1]}" not in distinct_positions:
                    debug_positions.append(pos)
                distinct_positions.add(f"{pos[0]}_{pos[1]}")
            else:
                continue
            break
        # self.debug(self.visual)
        # return len(distinct_positions) + 3

        # https://stackoverflow.com/a/77446062
        # debug_positions.sort(key=lambda l: l[0])
        # sorting by x, then y
        debug_positions = sorted(
            sorted(
                debug_positions, key = lambda x: x[1]
            ),
            key = lambda x: x[0]
        )
        for pos in debug_positions:
            new.write(f"{pos[0]} {pos[1]}\n")
    
        return f"expected: {count}, actual: {len(distinct_positions)}"
    
    def part2(self):
        pass

map = Map("input.txt")
# map.debug()
print(f"part 1: {map.part1()}")
# print(matrix)