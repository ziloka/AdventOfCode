import time
import functools

individual_blocks = []
diskmap = [*map(int, [*open("input.txt").read()])]
spaces = []
files = []
last_space = 0
for i, digit in enumerate(diskmap):
    if i % 2 == 0: # block file
        file_Id = int(i / 2)
        for _ in range(digit):
            individual_blocks.append(str(file_Id))
            files.append([len(individual_blocks) - 1, str(file_Id)])
    elif i % 2 == 1:
        for _ in range(digit):
            individual_blocks.append(".")
            spaces.append(len(individual_blocks) - 1)
        last_space = len(individual_blocks) - 1

space_idx = 0
files_idx = len(files) - 1
while spaces[space_idx] < files[files_idx][0]:
    s_block = spaces[space_idx]
    f_block, fileId = files[files_idx]
    individual_blocks[s_block] = fileId
    individual_blocks[f_block] = "."
    space_idx += 1
    files_idx -= 1
    # print(f"{idx} {space_idx}")
    # print(f"{s_block} {f_block} {last_space}")
    # print("".join(individual_blocks))

checksum = 0
for i, d in enumerate([*filter(lambda s: s != '.', individual_blocks)]):
    checksum += int(d) * i

start_time = time.time()
print(f"part 1: {checksum}")
print(f"took {time.time() - start_time:.2f}s")