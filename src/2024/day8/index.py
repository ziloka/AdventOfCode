from enum import Enum
import time

class OPTION(Enum):
    UP = 0 
    DOWN = 1
    BOTH = 2

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
                    if self.antennas.get(hz) == None:
                        self.antennas[hz] = [(r, c)]
                    else:
                        self.antennas[hz] += [(r, c)]
                    self.types.add(hz)
                self.positions.add((r, c))

    def is_valid(self, coords):
        return 0 <= coords[0] < self.num_table_rows and 0 <= coords[1] < self.num_table_cols

    def get_antinodes(self, anteannas, option=OPTION.BOTH):
        r1, c1 = anteannas[0]
        r2, c2 = anteannas[1]
        dr = r2 - r1
        dc = c2 - c1
        left_diagonal = dr >= 0 and dc <= 0
        right_diagonal = dr >= 0 and dc >= 0
        assert r2 > r1 or left_diagonal or right_diagonal

        upwards_cords = (r1 - dr, c1 - dc)
        downwards_cords = (r2 + dr, c2 + dc) 
        match option:
            case OPTION.UP:
                return [upwards_cords, anteannas[0]]
            case OPTION.DOWN:
                return [anteannas[1], downwards_cords]
            case OPTION.BOTH:
                return [upwards_cords, downwards_cords]
            case _:
                assert False

    def debug(self, antinodes):
        table = [["." for _ in range(self.num_table_cols)] for _ in range(self.num_table_rows)]
        for r, c, hz in [*antinodes]:
            table[r][c] = hz
        print( "\n".join(map(lambda row: "".join(row), table)))

    def part1(self):
        antinodes = set()
        for hz in self.types:
            for i in range(0, len(self.antennas[hz])):
                for j in range(i + 1, len(self.antennas[hz])):
                    if i != j:
                        n_ants = self.get_antinodes((self.antennas[hz][i], self.antennas[hz][j]))
                        for n_ant in n_ants:
                            if n_ant in self.positions:
                                antinodes.add(n_ant)
        return len(antinodes)

    def part2_helper(self):
        antinodes = set()
        for hz in self.types:
            antenna_positions = self.antennas[hz]

            for ant in antenna_positions:
                antinodes.add((ant[0], ant[1], hz))

            for i in range(len(antenna_positions)):
                for j in range(i + 1, len(antenna_positions)):
                    a1 = antenna_positions[i]
                    a2 = antenna_positions[j]

                    n_ants = self.get_antinodes((a1, a2))
                    for n_ant in n_ants:
                        if self.is_valid(n_ant):
                            antinodes.add((*n_ant, hz))

                    dr = a2[0] - a1[0]
                    dc = a2[1] - a1[1]

                    current = (a2[0] + dr, a2[1] + dc)
                    while self.is_valid(current):
                        antinodes.add((*current, hz))
                        current = (current[0] + dr, current[1] + dc)

                    current = (a1[0] - dr, a1[1] - dc)
                    while self.is_valid(current):
                        antinodes.add((*current, hz))
                        current = (current[0] - dr, current[1] - dc)
        return antinodes

    def part2(self):
        antinodes = self.part2_helper()
        return len(set((r, c) for r, c, _ in antinodes))

freqMap = FrequencyMap("input.txt")
start_time = time.time()
print(f"part 1: {freqMap.part1()}")
print(f"part 2: {freqMap.part2()}")
print(f"took {time.time() - start_time:.2f}s")