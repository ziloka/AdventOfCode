import time

MAX_HEIGHT = 9
class TopographicMap:

    def __init__(self, filename="example.txt"):
        self.map = {}
        topographic_list = open(filename).read().splitlines()
        self.nums_row = len(topographic_list)
        self.nums_col = len(topographic_list[0])
        for i, row_str in enumerate(topographic_list):
            for j, n in enumerate([*map(int, [*row_str])]):
                self.map[i, j] = n
                if n == 0:
                    self.pos = (i, j)

    def is_valid(self, row, col):
        return 0 <= row < self.nums_row and 0 <= col < self.nums_col

    def part1_helper(self, visited, pos, target = 1, result = 0):

        # while (len(stack)):


        visited[pos] = True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # visit adjacent nodes
            new_pos = (pos[0] + dr, pos[1] + dc)
            if self.is_valid(*new_pos) and new_pos not in visited and self.map[new_pos] == target: # not visited, and is adjacent
                if target == MAX_HEIGHT-1:
                    result += 1
                print(f"height: {target}, result: {result}")
                self.part1_helper(visited, new_pos, target+1, result)

        return result

    # iterative DFS approach
    def part1(self):
        source = self.pos
        visited = {}
        result = self.part1_helper(visited, source)
        return result
    

    def part2(self):    
        return

map = TopographicMap("example.txt")
time_start = time.time()
print(f"part 1: {map.part1()}")
print(f"part 2: {map.part2()}")
print(f"took {time.time() - time_start:.2f}s")