import math

class Waterfall:
    def __init__(self):
        sand_source = (500, 0)

        paths = []
        self.offset_x = math.inf
        self.max_x = 0
        self.max_y = 0
        for line in open("example.txt").readlines():
            path = []
            for coords in line.split(" -> "):
                x, y = map(int, coords.split(","))
                path.append((x, y))

                if x > self.max_x:
                    self.max_x = x
                if y + 1> self.max_y:
                    self.max_y = y + 1
                if x < self.offset_x:
                    self.offset_x = x
            paths.append(path)

        self.paths = paths
        self.matrix = [["."] * (self.max_x-self.offset_x) for _ in range(self.max_y)]
        self.place_object(sand_source, "+")
        self.place_rocks()

    def place_object(self, coords, object):
        # x coordinate is from the right, y coordinate is distance down
        coords = (coords[0] - self.offset_x, coords[1])
        self.matrix[coords[1]][coords[0]] = object

    def place_rocks(self):
        for path in self.paths:
            for i in range(len(path)-1):
                start_coord = path[i]
                end_coord = path[i+1]
                if start_coord[0] == end_coord[0]: # vertical
                    # x is from the right, so end_coord[0] < start_coord[0]
                    assert start_coord[1] < end_coord[1]
                    for y in range(start_coord[1], end_coord[1]+1):
                        self.place_object((start_coord[0], y), "#")
                elif start_coord[1] == end_coord[1]: # horizontal
                    print("got here")
                    for x in range(end_coord[0], start_coord[0]):
                        self.place_object((x, start_coord[1]), "#")
                else:
                    raise Exception("Invalid path")
                # self.debug()
            # exit()

    def debug(self):
        for line in self.matrix:
            print("".join(line))
        print()

    def start_sand(self):
        pass

waterfall = Waterfall()
waterfall.debug()