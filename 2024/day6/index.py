import time
from enum import Enum

class GUARD(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

class MOVEMENT:
    # assume guard is initially facing up
    def __init__(self, coords):
        self.coords = coords
        self.direction = GUARD.UP

    def forward(self):
        x, y = self.coords
        match self.direction:
            case GUARD.UP:
                return [x - 1, y]
            case GUARD.RIGHT:
                return [x, y + 1]
            case GUARD.DOWN:
                return [x + 1, y]
            case GUARD.LEFT:
                return [x, y - 1]
            case _:
                raise Exception(f"unexpected guard got: {self.direction}, expected {', '.join(map(lambda e: e, GUARD))}")

    # follow strict protocol, ONLY rotate clockwise in front of obstruction
    def turn(self):
        match self.direction:
            case GUARD.UP:
                return GUARD.RIGHT
            case GUARD.RIGHT:
                return GUARD.DOWN
            case GUARD.DOWN:
                return GUARD.LEFT
            case GUARD.LEFT:
                return GUARD.UP
            case _:
                raise Exception(f"unexpected guard got: {self.direction}, expected {', '.join(map(lambda e: e, GUARD))}")

class OBJECT(Enum):
    OBSTRUCTION = "#"
    EMPTY = "."

class PatrolRoute():
    def __init__(self, filename="example.txt"):
        self.init(filename)
    
    def init(self, filename):
        self.filename = filename
        self.valid_positions = set()
        self.obstacles = set()
        rows = open(filename).read().split("\n")
        for i, row in enumerate(rows):
            elements = list(row)
            for j, e in enumerate(elements):
                if e in [direction.value for direction in GUARD]: 
                    self.guard = MOVEMENT([i, j])
                elif e == OBJECT.OBSTRUCTION.value:
                    self.obstacles.add((i, j))
                self.valid_positions.add((i, j))
        self.init_guard_pos = (tuple(self.guard.coords), self.guard.direction)

    def part1(self):
        distinct_positions = set()
        while True:
            distinct_positions.add(tuple(self.guard.coords))

            coords = self.guard.forward()
            if tuple(coords) not in self.valid_positions:
                return distinct_positions

            if tuple(coords) in self.obstacles:
                self.guard.direction = self.guard.turn()
            else:
                self.guard.coords = coords

    def is_loop(self):
        distinct_positions = set()
        while True:
            # if guard is at the same position, facing the same direction, inf loop
            if (tuple(self.guard.coords), self.guard.direction) in distinct_positions:
                return True
            distinct_positions.add((tuple(self.guard.coords), self.guard.direction))

            coords = self.guard.forward()
            if tuple(coords) not in self.valid_positions:
                return False

            if tuple(coords) in self.obstacles:
                self.guard.direction = self.guard.turn()
            else:
                self.guard.coords = coords

    def part2(self, visited_positions):
        inf_loop_obstacles = []
        for road_block in visited_positions:
            self.guard.coords, self.guard.direction = self.init_guard_pos
            self.obstacles.add(road_block)

            if self.is_loop():
                inf_loop_obstacles.append(road_block)
            
            self.obstacles.remove(road_block)

        return len(inf_loop_obstacles)

patrol_route = PatrolRoute("input.txt")
start = time.time()

visited_positions = patrol_route.part1()
print(f"part 1: {len(visited_positions)}")

p2 = patrol_route.part2(visited_positions)
print(f"part 2: {p2}") # got 1681, actual is 1793

print(f"runtime: {time.time() - start:.2f}s")
