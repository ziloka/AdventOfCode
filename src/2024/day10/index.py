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

    def is_valid(self, row, col):
        return 0 <= row < self.nums_row and 0 <= col < self.nums_col

    # iterative DFS approach
    def get_trailheads(self, visited, pos):
        trailheads = 0
        stack = [(pos, 1)]
        while len(stack):
            pos, target_height = stack[-1]
            stack.pop()
            if pos not in visited:
                print(f"visited {pos}, {self.map[pos]}")
                if self.map[pos] == MAX_HEIGHT:
                    print(f"trailhead {self.map[pos]}")
                    trailheads += 1
                target_height += 1
                visited[pos] = True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # visit adjacent nodes
                new_pos = (pos[0] + dr, pos[1] + dc)
                if self.is_valid(*new_pos) and new_pos not in visited: # not visited
                    if self.map[new_pos]+1 == target_height:
                        stack.append((new_pos, target_height))
        return trailheads

    def part1(self):
        cumulative_score = 0
        for i in range(self.nums_row):
            for j in range(self.nums_col):
                if self.map[i, j] == 0:
                    source = (i, j)
                    visited = {}
                    trailheads = self.get_trailheads(visited, source)
                    cumulative_score += trailheads
        return cumulative_score
    

    def part2(self):    
        return

map = TopographicMap("input.txt")
time_start = time.time()
print(f"part 1: {map.part1()}")
print(f"part 2: {map.part2()}")
print(f"took {time.time() - time_start:.2f}s")