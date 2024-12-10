import time

def parse_part1(filename):
    individual_blocks = []
    diskmap = [*map(int, [*open(filename).read()])]
    spaces = []
    files = []
    for i, digit in enumerate(diskmap):
        if i % 2 == 0: # block file
            file_Id = int(i / 2)
            for _ in range(digit):
                individual_blocks.append(str(file_Id))
                files.append([len(individual_blocks) - 1, str(file_Id), digit])
        elif i % 2 == 1:
            for _ in range(digit):
                individual_blocks.append(".")
                spaces.append([len(individual_blocks) - 1, digit])
    return individual_blocks, spaces, files

def move_single_file_blocks(individual_blocks, spaces, files):
    space_idx = 0
    files_idx = len(files) - 1
    while spaces[space_idx][0] < files[files_idx][0]:
        s_block, _ = spaces[space_idx]
        f_block, fileId, _ = files[files_idx]
        individual_blocks[s_block] = fileId
        individual_blocks[f_block] = "."
        space_idx += 1
        files_idx -= 1

def calculate_checksum(individual_blocks):
    checksum = 0
    for i, d in enumerate([*filter(lambda s: s != '.', individual_blocks)]):
        checksum += int(d) * i
    return checksum
    
def part1(filename):
    individual_blocks, spaces, files = parse_part1(filename)
    move_single_file_blocks(individual_blocks, spaces, files)
    return calculate_checksum(individual_blocks)

def parse_part2(filename):
    individual_blocks = []
    diskmap = [*map(int, [*open(filename).read()])]
    spaces = []
    files = []
    for i, digit in enumerate(diskmap):
        if i % 2 == 0: # block file
            file_Id = int(i / 2)
            files.append([len(individual_blocks), str(file_Id), digit])
            for _ in range(digit):
                individual_blocks.append(str(file_Id))
        elif i % 2 == 1:
            spaces.append([len(individual_blocks), digit])
            for _ in range(digit):
                individual_blocks.append(".")
    return individual_blocks, spaces, files

def move_multiple_blocks(individual_blocks, spaces, files):
    for f_block, fileId, f_size in files[::-1]:
        best_start = None
        best_size = 0

        for s_block, s_size in spaces:
            if s_block < f_block and s_size >= f_size:
                if s_size > best_size:  
                    best_start = s_block
                    best_size = s_size

        if best_start is not None: 
            print("".join(individual_blocks))
            for i in range(best_start, best_start + f_size):
                individual_blocks[i] = fileId
            for i in range(f_block, f_block + f_size):
                individual_blocks[i] = "."

            for space in spaces:
                if space[0] == best_start:
                    space[1] -= f_size
                    space[0] += f_size
                    break

def part2(filename):
    individual_blocks, spaces, files = parse_part2(filename)
    move_multiple_blocks(individual_blocks, spaces, files)
    return calculate_checksum(individual_blocks)

filename = "example.txt"
start_time = time.time()
print(f"part 1: {part1(filename)}")
print(f"part 2: {part2(filename)}")
print(f"took {time.time() - start_time:.2f}s")