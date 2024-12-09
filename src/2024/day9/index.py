import time

def parse(filename="example.txt"):
    individual_blocks = []
    diskmap = [*map(int, [*open(filename).read()])]
    spaces = []
    files = []
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
    return individual_blocks, spaces, files

def move_single_file_blocks(individual_blocks, spaces, files):
    space_idx = 0
    files_idx = len(files) - 1
    while spaces[space_idx] < files[files_idx][0]:
        s_block = spaces[space_idx]
        f_block, fileId = files[files_idx]
        individual_blocks[s_block] = fileId
        individual_blocks[f_block] = "."
        space_idx += 1
        files_idx -= 1

def calculate_checksum(individual_blocks):
    checksum = 0
    for i, d in enumerate([*filter(lambda s: s != '.', individual_blocks)]):
        checksum += int(d) * i
    return checksum
    
def part1(individual_blocks, spaces, files):
    move_single_file_blocks(individual_blocks, spaces, files)
    return calculate_checksum(individual_blocks)

# def move_multiple_blocks(individual_blocks, spaces, files):
#     space_idx = 0
#     files_idx = len(files) - 1
#     while spaces[space_idx] < files[files_idx][0]:
#         s_block = spaces[space_idx]
#         f_block, fileId = files[files_idx]
#         individual_blocks[s_block] = fileId
#         individual_blocks[f_block] = "."
#         space_idx += 1
#         files_idx -= 1

# def part2(individual_blocks, spaces, files):
#     move_multiple_blocks(individual_blocks, spaces, files)
#     return calculate_checksum(individual_blocks)

individual_blocks, spaces, files = parse("input.txt")
start_time = time.time()
print(f"part 1: {part1(individual_blocks, spaces, files)}")
# print(f"part 2: {part2(individual_blocks, spaces, files)}")
print(f"took {time.time() - start_time:.2f}s")