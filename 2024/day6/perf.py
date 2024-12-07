import time
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
        self.filename = filename
        self.matrix = []
        rows = open(filename).read().split("\n")
        self.obstacles = set()
        for i, row in enumerate(rows):
            elements = list(row)
            for j, e in enumerate(elements):
                if e in [e.value for e in GUARD]: 
                    self.guard_pos = [i, j]
                elif e == OBJECT.OBSTRUCTION.value:
                    self.obstacles.add((i, j))
            # self.obstacles[i] = [e == OBJECT.OBSTRUCTION.value for e in elements]
            self.matrix.append(elements)
        self.init_guard_pos = (tuple(self.guard_pos), self.get_element(self.guard_pos))

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

    # if last position is None, end of path, end program
    def forward(self):
        positions = []
        candidate_obstacles = []
        guard = self.get_element(self.guard_pos)
        # go forward
        if guard == GUARD.UP.value and self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]-1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.guard_pos[0] -= 1

                if not self.is_valid_pos(self.guard_pos):
                    return ([*positions, None], candidate_obstacles)
                positions.append(tuple(self.guard_pos.copy()))
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.UP.value

                # check if placing obstruction in front of guard will make inf loop

                # same element, checked 19 times for a 10x10 matrix
                for colIdx in range(self.guard_pos[1], len(self.matrix[0])):
                    if self.get_element([self.guard_pos[0], colIdx]) == OBJECT.OBSTRUCTION.value:
                        # print([self.guard_pos[0]-1, self.guard_pos[1]])
                        candidate_obstacles.append([self.guard_pos[0]-1, self.guard_pos[1]])
                        break
        elif guard == GUARD.DOWN.value and self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0]+1, self.guard_pos[1]]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.guard_pos[0] += 1

                if not self.is_valid_pos(self.guard_pos):
                    return ([*positions, None], candidate_obstacles)
                positions.append(tuple(self.guard_pos.copy()))
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.DOWN.value

                # check if placing obstruction in front of guard will make inf loop
                for colIdx in range(0, self.guard_pos[1]):
                    if self.get_element([self.guard_pos[0], colIdx]) == OBJECT.OBSTRUCTION.value:
                        # print([self.guard_pos[0]+1, self.guard_pos[1]])
                        candidate_obstacles.append([self.guard_pos[0]+1, self.guard_pos[1]])
                        break

        elif guard == GUARD.LEFT.value and self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]-1]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.guard_pos[1] -= 1

                if not self.is_valid_pos(self.guard_pos):
                    return ([*positions, None], candidate_obstacles)
                positions.append(tuple(self.guard_pos.copy()))
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.LEFT.value

                # check if placing obstruction in front of guard will make inf loop
                for rowIdx in range(0, self.guard_pos[0]):
                    if self.get_element([rowIdx, self.guard_pos[0]]) == OBJECT.OBSTRUCTION.value:
                        # print([self.guard_pos[0], self.guard_pos[1]-1])
                        candidate_obstacles.append([self.guard_pos[0], self.guard_pos[1]-1])
                        break
        elif guard == GUARD.RIGHT.value and self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
            while self.get_element([self.guard_pos[0], self.guard_pos[1]+1]) != OBJECT.OBSTRUCTION.value:
                self.set_element(self.guard_pos, OBJECT.EMPTY.value)
                self.guard_pos[1] += 1

                if not self.is_valid_pos(self.guard_pos):
                    return ([*positions, None], candidate_obstacles)
                positions.append(tuple(self.guard_pos.copy()))
                self.matrix[self.guard_pos[0]][self.guard_pos[1]] = GUARD.RIGHT.value

                for colIdx in range(self.guard_pos[1], len(self.matrix)):
                    if self.get_element([self.guard_pos[0], colIdx]) == OBJECT.OBSTRUCTION.value:
                        # print([self.guard_pos[0], self.guard_pos[1]+1])
                        candidate_obstacles.append([self.guard_pos[0], self.guard_pos[1]+1])
                        break
        return (tuple(positions), candidate_obstacles)
    
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
        positions, obstacles = self.forward()
        if positions[-1] == None:
            return positions, obstacles
        self.turn()
        return positions, obstacles
    
    def inf_loop_helper(self):
        positions, _ = self.forward()
        if len(positions) == 0 or positions[-1] == None:
            return positions
        self.turn()
        return positions
        
    def driver_code(self):
        debug_positions = []
        obstacles_candidates = []
        distinct_positions = set()
        # https://stackoverflow.com/a/654002
        while True:
            positions, road_blocks = self.execute_protocol()
            obstacles_candidates.append(road_blocks)
            for pos in positions:
                if pos == None:
                    break
                if f"{pos[0]}_{pos[1]}" not in distinct_positions:
                    debug_positions.append(pos)
                distinct_positions.add(f"{pos[0]}_{pos[1]}")
            else:
                continue
            break

        obstacles = []
        for road_block in obstacles_candidates:
            for i, (x, y) in enumerate(road_block):
                if not self.is_valid_pos([x, y]):
                    continue
                self.guard_pos = list(self.init_guard_pos[0])
                self.set_element(self.init_guard_pos[0], self.init_guard_pos[1])

                # remove the last obstruction
                if i > 0:
                    self.matrix[road_block[i-1][0]][road_block[i-1][1]] = OBJECT.EMPTY.value
                self.matrix[x][y] = OBJECT.OBSTRUCTION.value
                history_positions = []
                while True:
                    positions = self.inf_loop_helper()
                    history_positions.append(positions)
                    if len(positions) == 0 or positions[-1] == None:
                        break
                    else:
                        # check if last n positions are the same
                        for j in range(1, len(history_positions)//2):
                            # if guard goes on the same path twice, it is an inf loop
                            # so compare last n, with last n - 2n, and then compare first half to second half
                            # but this is vulnerable to hash collisions
                            if  hash(tuple(history_positions[-j:])) ==  hash(tuple(history_positions[2*-j:-j])):
                                # self.matrix[x][y] = "O"
                                # self.debug(self.matrix)
                                obstacles.append([x, y])
                                print(f"now {len(obstacles)} obstacles")
                                break
                        else:
                            continue
                        break

        return len(distinct_positions), len(obstacles)

patrol_route = PatrolRoute("input.txt")
start = time.time()
print(f"dealing with {len(patrol_route.matrix)}x{len(patrol_route.matrix[0])} matrix")
p1, p2 = patrol_route.driver_code()
print(f"part 1: {p1}")

# example edge case
# .#..
# ...#
# ....
# .^#.
print(f"part 2: {p2}") # got 1681, actual is 1793
# print(matrix)
print(f"runtime: {time.time() - start:.2f}s")


# Get-Process | select name,starttime,id | select-string -pattern "python"
# pip install py-spy
# py-spy record --python ./day6/pref.py
# py-spy top -- python index.py
# or do ongoing process
# py-spy record profile.svg --pid PID


# git clone https://git.sr.ht/~mariell/aoc.git
# cargo run -- year2024 6 2