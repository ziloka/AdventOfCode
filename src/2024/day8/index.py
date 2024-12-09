from enum import Enum
import time

# diagonally
class Direction(Enum):
    UP = 0 
    DOWN = 1 

class FrequencyMap:
    def __init__(self, filename="example.txt"):
        city_map = open(filename, encoding="utf8").read().splitlines()
        self.positions = set()
        self.antennas = dict()
        self.types = set()
        self.num_table_rows = len(city_map)
        for r, line in enumerate(city_map):
            row = [*line]
            self.num_table_cols = len(row)
            for c, hz in enumerate(row):
                if hz != "." and hz != "#":
                    if self.antennas.get(hz) is None:
                        self.antennas[hz] = [(r, c)]
                    else:
                        self.antennas[hz] += [(r, c)]
                    self.types.add(hz)
                self.positions.add((r, c))

    # first element is going upwards, second element is downwards
    # for left diagonal, arr[0] is upwards, arr[1] is downwards
    def get_antinodes(self, anteannas):
        r1, c1 = anteannas[0]
        r2, c2 = anteannas[1]
        dr = r2 - r1
        dc = c2 - c1
        left_diagonal = dr >= 0 and dc <= 0
        right_diagonal = dr >= 0 and dc >= 0
        assert r2 > r1 or left_diagonal or right_diagonal
        return [(r1 - dr, c1 - dc), (r2 + dr, c2 + dc)]

    def debug(self, antinodes):
        table_string = ""
        for r in range(self.num_table_rows):
            for c in range(self.num_table_cols):
                if (r, c) in antinodes:
                    table_string += antinodes[(r, c)]
                else:
                    table_string += "."
            table_string += "\n"
        print(table_string)

    def part1(self):
        antinodes = dict()
        for hz in self.types:
            for i in range(0, len(self.antennas[hz])):
                for j in range(i + 1, len(self.antennas[hz])):
                    if i != j:
                        n_ants = self.get_antinodes((self.antennas[hz][i], self.antennas[hz][j]))
                        for n_ant in n_ants:
                            if n_ant in self.positions:
                                antinodes[n_ant] = hz
        return len(antinodes)

    def part2(self):
        antinodes = dict()
        for hz in self.types:
            for i in range(0, len(self.antennas[hz])):
                for j in range(i + 1, len(self.antennas[hz])):
                    if i != j:
                        n_ants = self.get_antinodes((self.antennas[hz][i], self.antennas[hz][j]))
                        antinode_position_history = [self.antennas[hz][i], self.antennas[hz][j]]
                        switchUsed = False
                        continueOneDirection = False
                        direction = None
                        while not switchUsed or not continueOneDirection:
                            assert len(n_ants) == 2

                            if switchUsed:
                                if direction == Direction.UP:
                                    n_ants = [
                                        self.get_antinodes((antinode_position_history[-1], n_ants[1]))[0],
                                        n_ants[0]
                                    ]
                                elif direction == Direction.DOWN:
                                    n_ants = [
                                        n_ants[1],
                                        self.get_antinodes((antinode_position_history[-1], n_ants[1]))[1]
                                    ]
                                    if n_ants[0] == n_ants[1]:
                                        break
                                else:
                                    assert False
                            for n, n_ant in enumerate(n_ants):
                                if n_ant in self.positions:
                                    antinodes[n_ant] = hz
                                    antinode_position_history.append(n_ant)
                                else:
                                    if n == 0 and not switchUsed: # go downwards instead
                                        n_ants = [
                                            n_ants[1],
                                            self.get_antinodes((antinode_position_history[-1], n_ants[1]))[1]
                                        ]
                                        antinode_position_history.append(n_ants[0])
                                        direction = Direction.DOWN
                                        switchUsed = True
                                        # print("got here")
                                    elif n == 1 and not switchUsed: # go upwards instead
                                        n_ants = [
                                            self.get_antinodes((antinode_position_history[-1], n_ants[1]))[0],
                                            n_ants[0]
                                        ]
                                        antinode_position_history.append(n_ants[1])
                                        switchUsed = True
                                        direction = Direction.UP
                                        # print("got here 2")
                                    else:
                                        print("is this the end?")
                                        break
                            else:
                                continue        
                            break

        self.debug(antinodes)
        return len(antinodes)

freqMap = FrequencyMap("example.txt")
start_time = time.time()
print(f"part 1: {freqMap.part1()}")
print(f"part 2: {freqMap.part2()}")
print(f"took {time.time() - start_time:.2f}s")