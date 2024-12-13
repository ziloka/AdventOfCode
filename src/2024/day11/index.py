import time

def transform(stone, memo):
    if stone in memo:
        return memo[stone]
    if stone == 0:
        result = [1]
    elif len(str(stone)) % 2 == 0:
        stone_string = str(stone)
        half = len(stone_string) // 2
        left_half = int(stone_string[:half])
        right_half = int(stone_string[half:])
        result = [left_half, right_half]
    else:
        result = [stone * 2024]
    memo[stone] = result
    return result

def pebble(stones, n):
    stones = stones.copy()
    memo = {}
    for _ in range(n):
        new_stones = []
        for stone in stones:
            new_stones.extend(transform(stone, memo))
        stones = new_stones
    return stones

# Read input stones
stones = [*map(int, open("input.txt").read().split())]

# Measure execution time
start_time = time.time()

# Part 1
print(f"part 1: {len(pebble(stones, 25))}")

# Uncomment below for part 2 (it will be resource-intensive)
print(f"part 2: {len(pebble(stones, 75))}")

print(f"took {time.time() - start_time:.2f}s")
