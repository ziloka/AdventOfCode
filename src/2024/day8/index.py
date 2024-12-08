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

    def get_antinodes(self, anteannas):
        r1, c1 = anteannas[0]
        r2, c2 = anteannas[1]
        dr = r2 - r1
        dc = c2 - c1
        assert r2 > r1
        if (dr > 0 and dc < 0) or (dr > 0 and dc > 0): # \, /
            return [(r1 - dr, c1 - dc), (r2 + dr, c2 + dc)]
        else:
            raise Exception(f"unexpected coords: {anteannas} {dr} {dc}")

    def part1(self):
        antinodes = dict()
        for hz in self.types:
            # for every 2n antennas exists, 2^n possible antinodes exist
            # make each i, and j pair unique
            for i in range(0, len(self.antennas[hz])):
                for j in range(i + 1, len(self.antennas[hz])):
                    if i != j:
                        # print(f"{hz} {i} {j}")
                        n_ants = self.get_antinodes((self.antennas[hz][i], self.antennas[hz][j]))
                        for n_ant in n_ants:
                            if  n_ant in self.positions:
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

freqMap = FrequencyMap("input.txt")
print(f"part 1: {freqMap.part1()}")
