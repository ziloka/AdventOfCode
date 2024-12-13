import time

def blink(stones, n):
    stones = stones.copy()
    for _ in range(n):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
                i += 1
            elif len(str(stones[i])) % 2 == 0:
                stone_string = str(stones[i])
                half = len(stone_string) // 2
                leftHalf = int(stone_string[:half])
                rightHalf = int(stone_string[half:])
                stones[i] = leftHalf
                stones.insert(i + 1, rightHalf)
                i += 2
            else:
                stones[i] *= 2024
                i += 1
    return stones

stones = [*map(int, open("input.txt").read().split(" "))]
start_time = time.time()
print(f"part 1: {len(blink(stones, 25))}")
# print(f"part 1: {len(blink(stones, 75))}")
print(f"took {time.time() - start_time:.2f}s")