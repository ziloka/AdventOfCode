import time

MAX_HEIGHT = 9
class HikingTrails:

    def __init__(self, filename="example.txt"):
        self.map = {}
        topographic_list = open(filename).read().splitlines()
        for i, row_str in enumerate(topographic_list):
            for j, n in enumerate([*map(int, [*row_str])]):
                self.map[i, j] = n

    # iterative DFS approach
    def get_num_trailheads(self, visited, pos):
        trailheads = 0
        stack = [(pos, 1)]
        while len(stack):
            pos, target_height = stack[-1]
            stack.pop()
            if pos not in visited:
                target_height += 1
                visited[pos] = True
                if self.map[pos] == MAX_HEIGHT:
                    trailheads += 1
                
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # visit adjacent nodes
                new_pos = (pos[0] + dr, pos[1] + dc)
                if new_pos in self.map and new_pos not in visited: # not visited
                    if self.map[new_pos]+1 == target_height:
                        stack.append((new_pos, target_height))
        return trailheads

    def part1(self):
        cumulative_score = 0
        for source in [*filter(lambda p: self.map[p] == 0, self.map)]:
            trailheads = self.get_num_trailheads({}, source)
            cumulative_score += trailheads
        return cumulative_score
    
    def debug(self, trail):
        cols = [j for _, j in self.map.keys()][-1]
        rows = [j for _, j in self.map.keys()][-1]

        table = [["." for _ in range(cols + 1)] for _ in range(rows + 1)]
        for r, c in trail:
            table[r][c] = self.map[r, c]

        print("\n".join(map(lambda row: "".join(map(str, row)), table)))
        print()

    # iterative DFS approach
    def get_num_ratings(self, visited, pos):
        hiking_trails = []
        trail = set()
        stack = [(pos, 1)]
        while len(stack):
            pos, target_height = stack[-1]
            stack.pop()
            if pos not in visited:
                visited[pos] = True
                trail.add(pos)
                # print(f"{pos} {target_height}")
                if self.map[pos] == MAX_HEIGHT:
                    hiking_trails.append(trail)
                    self.debug(trail)
                    trail = set()
                    target_height = 1
                    # print()
                else:
                    target_height += 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # visit adjacent nodes
                new_pos = (pos[0] + dr, pos[1] + dc)
                if new_pos in self.map and new_pos not in visited: # not visited
                    # print(f"{new_pos} {target_height}")
                    if self.map[new_pos]+1 == target_height:
                        stack.append((new_pos, target_height))
        return len(hiking_trails)
    
    def part2(self):    
        trailheads = self.get_num_ratings({}, (0, 4))
        print(trailheads)
        # cumulative_score = 0
        # for source in [*filter(lambda p: self.map[p] == 0, self.map)]:
        #     trailheads = self.get_num_ratings({}, source)
        #     cumulative_score += trailheads
        # return cumulative_score

hiking_trails = HikingTrails("example.txt")
time_start = time.time()
print(f"part 1: {hiking_trails.part1()}")
print(f"part 2: {hiking_trails.part2()}")
print(f"took {time.time() - time_start:.2f}s")