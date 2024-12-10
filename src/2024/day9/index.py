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
    space_idx = 0
    jump = True
    remainingSpace = 0
    for f_block, fileId, f_size in files[::-1]:
        s_block, s_size = spaces[space_idx]
        if jump:
            remainingSpace = s_size
            jump = False
        
        print(f"Id: {fileId}")
        if f_size <= remainingSpace:
            remainingSpace -= f_size
            jump = False
            for i in range(s_block, s_block + s_size):
                individual_blocks[i] = fileId
            # print(f_block, f_block + f_size)
            for i in range(f_block, f_block + f_size):
                individual_blocks[i] = "."
            print("".join(individual_blocks))
        
        if remainingSpace == 0:
            space_idx += 1
            jump = True
        
def part2(filename):
    individual_blocks, spaces, files = parse_part2(filename)
    move_multiple_blocks(individual_blocks, spaces, files)
    return calculate_checksum(individual_blocks)

filename = "example.txt"
start_time = time.time()
print(f"part 1: {part1(filename)}")
print(f"part 2: {part2(filename)}")
print(f"took {time.time() - start_time:.2f}s")