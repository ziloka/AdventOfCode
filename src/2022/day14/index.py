# https://www.reddit.com/r/adventofcode/comments/zlu722/2022_day_14_part_2_i_optimized_my_code_to_run/

import time
from enum import Enum
import math

class OBJECT(Enum):
    ROCK = "#"
    SAND = "o"
    SOURCE = "+"
    AIR = "."

class Waterfall:
    def __init__(self, filename="example.txt"):
        self.sand_source = (500, 0)

        paths = []
        self.offset_x = math.inf
        self.max_x = 0
        self.max_y = 0
        for line in open(filename).readlines():
            path = []
            for absolute_coords in line.split(" -> "):
                x, y = map(int, absolute_coords.split(","))
                path.append((x, y))

                if x + 1 > self.max_x:
                    self.max_x = x + 1
                if y + 1> self.max_y:
                    self.max_y = y + 1
                if x < self.offset_x:
                    self.offset_x = x
            paths.append(path)

        self.paths = paths
        self.matrix = [["."] * (self.max_x-self.offset_x) for _ in range(self.max_y)]
        self.matrix_set(self.sand_source, OBJECT.SOURCE.value)
        self.place_rocks()

    def normalize_cords(self, absolute_coords):
        return (absolute_coords[0] - self.offset_x, absolute_coords[1])

    def matrix_set(self, relative_coords, object):
        # x coordinate is from the right, y coordinate is distance down
        relative_coords = self.normalize_cords(relative_coords) # (X, Y)
        self.matrix[relative_coords[1]][relative_coords[0]] = object

    def place_rocks(self):
        for path in self.paths:
            for i in range(len(path)-1):
                start_coord = path[i]
                end_coord = path[i+1]
                if start_coord[0] == end_coord[0]: # vertical
                    # x is from the right, so end_coord[0] < start_coord[0]
                    dist = [start_coord[1], end_coord[1]]
                    dist.sort()
                    for y in range(dist[0], dist[1]+1):
                        self.matrix_set((start_coord[0], y), OBJECT.ROCK.value)
                elif start_coord[1] == end_coord[1]: # horizontal
                    # assert end_coord[0] < start_coord[0]
                    dist = [start_coord[0], end_coord[0]]
                    dist.sort()
                    for x in range(dist[0], dist[1]+1):
                        self.matrix_set((x, start_coord[1]), OBJECT.ROCK.value)
                else:
                    raise Exception("Invalid path")

    def debug(self):
        for line in self.matrix:
            print("".join(line))
        print()

    def part1_matrix_get(self, absolute_coords):
        rel_coords = self.normalize_cords(absolute_coords) # (X, Y)
        
        # if invalid position return None
        if 0 <= rel_coords[1] < len(self.matrix) and 0 <= rel_coords[0] < len(self.matrix[0]):
            return self.matrix[rel_coords[1]][rel_coords[0]]

    def part1_sand_unit_movement_helper(self, abs_sand_unit):
        while abs_sand_unit[1] < self.max_y and self.part1_matrix_get((abs_sand_unit[0], abs_sand_unit[1]+1)) == OBJECT.AIR.value:
            abs_sand_unit[1] += 1

        # not free falling
        # try moving one step down to the right
        if self.part1_matrix_get((abs_sand_unit[0]+1, abs_sand_unit[1]+1)) == None or self.part1_matrix_get((abs_sand_unit[0]-1, abs_sand_unit[1]+1)) == None:
            return None
        elif self.part1_matrix_get((abs_sand_unit[0]-1, abs_sand_unit[1]+1)) == OBJECT.AIR.value:
            abs_sand_unit[1] += 1
            abs_sand_unit[0] -= 1
        elif self.part1_matrix_get((abs_sand_unit[0]+1, abs_sand_unit[1]+1)) == OBJECT.AIR.value: 
            abs_sand_unit[1] += 1
            abs_sand_unit[0] += 1
        else:
            return abs_sand_unit
        return self.part1_sand_unit_movement_helper(abs_sand_unit)

    def part1_start_sand(self):
        counter = 0
        while self.part1_matrix_get((self.sand_source[0], self.sand_source[1]+2)) != OBJECT.SOURCE.value:
            new_abs_sand_unit = self.part1_sand_unit_movement_helper([self.sand_source[0], self.sand_source[1]])
            if new_abs_sand_unit == None:
                # self.debug()
                break
            self.matrix_set(new_abs_sand_unit, OBJECT.SAND.value)
            counter += 1
        return counter

    def part2_matrix_get(self, absolute_coords):
        # expand the matrix, horizontally, check if matrix needs to be expanded leftwards or rightwards
        if absolute_coords[0] < self.offset_x:
            n = self.offset_x - absolute_coords[0]
            self.offset_x = absolute_coords[0]
            # add n columns to each row starting on the left and going to the left
            for i in range(len(self.matrix)-1):
                self.matrix[i] = [OBJECT.AIR.value] * n + self.matrix[i]
            self.matrix[-1] = [OBJECT.ROCK.value] * n + self.matrix[-1]
        elif absolute_coords[0] >= self.max_x:
            # add n columns to each row starting on the right and going to the right
            n = absolute_coords[0] - self.max_x + 1
            self.max_x = absolute_coords[0] + 1
            for i in range(len(self.matrix)-1):
                self.matrix[i] = self.matrix[i] + [OBJECT.AIR.value] * n
            self.matrix[-1] = [OBJECT.ROCK.value] * n + self.matrix[-1]
        # if invalid position return None
        rel_coords = self.normalize_cords(absolute_coords) # (X, Y)
        if 0 <= rel_coords[1] < len(self.matrix):
            return self.matrix[rel_coords[1]][rel_coords[0]]

    # this is the slow section
    def part2_sand_unit_movement_helper(self, abs_sand_unit):
        while abs_sand_unit[1] < self.max_y and self.part2_matrix_get((abs_sand_unit[0], abs_sand_unit[1]+1)) == OBJECT.AIR.value:
            abs_sand_unit[1] += 1

        # not free falling, try moving one step down to the right
        if self.part2_matrix_get((abs_sand_unit[0]-1, abs_sand_unit[1]+1)) == OBJECT.AIR.value:
            abs_sand_unit[1] += 1
            abs_sand_unit[0] -= 1
        elif self.part2_matrix_get((abs_sand_unit[0]+1, abs_sand_unit[1]+1)) == OBJECT.AIR.value: 
            abs_sand_unit[1] += 1
            abs_sand_unit[0] += 1
        else:
            return abs_sand_unit
        return self.part2_sand_unit_movement_helper(abs_sand_unit)
    
    def part2_start_sand(self):
        self.matrix = [["."] * (self.max_x-self.offset_x) for _ in range(self.max_y + 2)]
        for i in range(len(self.matrix[0])):
            self.matrix[-1][i] = OBJECT.ROCK.value
        self.matrix_set(self.sand_source, OBJECT.SOURCE.value)
        self.place_rocks()

        counter = 0
        while self.part2_matrix_get((self.sand_source[0], self.sand_source[1])) != OBJECT.SAND.value:
            new_abs_sand_unit = self.part2_sand_unit_movement_helper([self.sand_source[0], self.sand_source[1]])
            if new_abs_sand_unit == None:
                self.debug()
                break
            self.matrix_set(new_abs_sand_unit, OBJECT.SAND.value)
            counter += 1
        return counter

waterfall = Waterfall("input.txt")
print(f"part 1: {waterfall.part1_start_sand()}")
start = time.time()
print(f"part 2: {waterfall.part2_start_sand()}")
print(f"took: {time.time() - start:.2f}s")