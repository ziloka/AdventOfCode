from enum import Enum

class GUARD(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

class ROTATION(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class OBJECT(Enum):
    OBSTRUCTION = "#"
    EMPTY = "."

class PatrolRoute():
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

    def forward(self):
        positions = []
        guard = self.get_element(self.guard_pos)
        # go forward
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
        return positions
    
    # follow strict protocol, ONLY rotate clockwise in front of obstruction
    def turn(self):
        guard = self.get_element(self.guard_pos)
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
                raise Exception(f"unexpected guard got: {guard}, expected {', '.join(map(lambda e: e.value, GUARD))}")

    def execute_protocol(self):
        positions = self.forward()
        if positions[-1] == None:
            return positions
        self.turn()
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
        # trying placing an obstruction on the right side of the guard to make inf loop

        pass
    def part2(self):
        self.init()


patrol_route = PatrolRoute("input.txt")
print(f"part 1: {patrol_route.part1()}")
# print(matrix)