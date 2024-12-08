def parse(filename="example.txt"):
    city_map = open(filename).read().splitlines()
    positions = set()
    antennas = dict()
    types = set()
    for r, line in enumerate(city_map):
        for c, hz in enumerate([*line]):
            if hz != ".":
                if antennas.get(hz) == None:
                    antennas[hz] = [(r, c)]
                else:
                    antennas[hz] += [(r, c)]
                types.add(hz)
            positions.add((r, c))

    return types, antennas, positions

antinodes = set()
types, antennas, positions = parse()
for hz in types:
    # every n antennas exists, 2^n possible antinodes exist
    for i in range(0, len(antennas[hz]), 2):    
        r1, c1 = antennas[hz][i]
        r2, c2 = antennas[hz][i+1]

        dr = r2 - r1
        dc = c2 - c1

        # determine antinode position
        n_ants = [(r1 + dr, c1 + dc), (r2 - dr, r2 - dc)]
        print(n_ants)
        for n_ant in n_ants:
            if n_ant in positions:
                antinodes.add(n_ant)
# print(antinodes)
print(len(antinodes))