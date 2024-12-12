import time

MAX_HEIGHT = 9
class TopographicMap:

    def __init__(self, filename="example.txt"):
        self.map = {}
        topographic_list = open(filename).read().splitlines()
        for i, row_str in enumerate(topographic_list):
            for j, n in enumerate([*map(int, [*row_str])]):
                self.map[i, j] = n

    # iterative DFS approach
    def get_trailheads(self, visited, pos):
        trailheads = 0
        stack = [(pos, 1)]
        while len(stack):
            pos, target_height = stack[-1]
            stack.pop()
            if pos not in visited:
                if self.map[pos] == MAX_HEIGHT:
                    trailheads += 1
                target_height += 1
                visited[pos] = True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # visit adjacent nodes
                new_pos = (pos[0] + dr, pos[1] + dc)
                if new_pos in self.map and new_pos not in visited: # not visited
                    if self.map[new_pos]+1 == target_height:
                        stack.append((new_pos, target_height))
        return trailheads

    def part1(self):
        cumulative_score = 0
        for source in [*filter(lambda p: self.map[p] == 0, self.map)]:
            trailheads = self.get_trailheads({}, source)
            cumulative_score += trailheads
        return cumulative_score
    
    def part2(self):    
        return

map = TopographicMap("example.txt")
time_start = time.time()
print(f"part 1: {map.part1()}")
print(f"part 2: {map.part2()}")
print(f"took {time.time() - time_start:.2f}s")