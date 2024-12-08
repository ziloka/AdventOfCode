from enum import Enum

class ORIENTATION(Enum):
    VERTICAL = 1
    HORIZONTAL = 2
    LEFT_DIAGONAL = 3 # \
    RIGHT_DIAGONAL = 4 # /

class FrequencyMap:
    def __init__(self, filename="example.txt"):
        self.city_map = open(filename, encoding="utf8").read().splitlines()
        self.positions = set()
        self.antennas = dict()
        self.types = set()
        self.num_table_rows = len(self.city_map)
        for r, line in enumerate(self.city_map):
            row = [*line]
            self.num_table_cols = len(row)
            for c, hz in enumerate(row):
                if hz != ".":
                    if self.antennas.get(hz) is None:
                        self.antennas[hz] = [(r, c)]
                    else:
                        self.antennas[hz] += [(r, c)]
                    self.types.add(hz)
                self.positions.add((r, c))

    def direction(self, coords):
        r1, c1 = coords[0]
        r2, c2 = coords[1]
        dr = r2 - r1
        dc = c2 - c1
        if dr == 0:
            return ORIENTATION.HORIZONTAL
        if dc == 0:
            return ORIENTATION.VERTICAL
        if dr == dc:
            return ORIENTATION.LEFT_DIAGONAL
        if -dr == dc:
            return ORIENTATION.RIGHT_DIAGONAL

    def get_antinodes(self, coords):
        r1, c1 = coords[0]
        r2, c2 = coords[1]
        dr = r2 - r1
        dc = c2 - c1
        if dr == 0:# LEFT and RIGHT
            return [(r1, c1 - 1), (r1, c1 + 1)]
        if dc == 0:
            return [(r1 - 1, c1), (r1 + 1, c1)]
        if dr == dc:
            return [(r1 - 1, c1 - 1), (r1 + 1, c1 + 1)]
        if -dr == dc:
            return [(r1 - 1, c1 + 1), (r1 + 1, c1 - 1)]

    def part1(self):
        antinodes = dict()
        for hz in self.types:
            # for every 2n antennas exists, 2^n possible antinodes exist
            # make each i, and j pair unique
            for i in range(0, len(self.antennas[hz])):
                for j in range(i + 1, len(self.antennas[hz])):
                    if i != j:
                        r1, c1 = self.antennas[hz][i]
                        r2, c2 = self.antennas[hz][j]

                        dr = abs(r2 - r1)
                        dc = abs(c2 - c1)

                        # determine antinode position

                        # these antinodes are only for left diagonal though
                        n_ants = [(r1 - dr, c1 - dc), (r2 + dr, r2 + dc)]
                        valid = True
                        for n_ant in n_ants:
                            if n_ant not in self.positions:
                                valid = False
                                break
                        if valid and n_ants[0] not in antinodes and n_ants[1] not in antinodes:
                            for n_ant in n_ants:
                                antinodes[n_ant] = hz
        self.debug(antinodes)
        return len(antinodes)

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

freqMap = FrequencyMap()
print(f"part 1: {freqMap.part1()}")
