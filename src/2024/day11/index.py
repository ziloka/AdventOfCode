from functools import cache
import time

def transform(stone):
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
    return result

@cache
def blink(stones, blinks_left):
    if blinks_left == 0:
        return len(stones)
    
    return sum(blink(tuple(transform(stone)),  blinks_left - 1) for stone in stones)

stones = tuple([*map(int, open("input.txt").read().split())])

start_time = time.time()
print(f"part 1: {blink(stones, 25)}")
print(f"part 2: {blink(stones, 75)}")

print(f"took {time.time() - start_time:.2f}s")
