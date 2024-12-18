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
        
        for s_block, s_size in spaces:
            if s_block < f_block and s_size >= f_size:
                best_start = s_block
                break

        if best_start is not None:
            for i in range(f_block, f_block + f_size):
                individual_blocks[i] = '.'

            for i in range(best_start, best_start + f_size):
                individual_blocks[i] = str(fileId)
            
            for index in range(len(spaces)):
                if spaces[index][0] == best_start:
                    new_start = best_start + f_size
                    new_size = spaces[index][1] - f_size
                    if new_size == 0:
                        spaces.pop(index)
                    else:
                        spaces[index] = (new_start, new_size)
                    break

def part2(filename):
    individual_blocks, spaces, files = parse_part2(filename)
    move_multiple_blocks(individual_blocks, spaces, files)
    return calculate_checksum(individual_blocks)

filename = "input2.txt.HARDER"
start_time = time.time()
print(f"part 1: {part1(filename)}")
print(f"part 2: {part2(filename)}")
print(f"took {time.time() - start_time:.2f}s")

# some more if you want to torture your brain
# https://www.reddit.com/r/adventofcode/comments/1haauty/2024_day_9_part_2_bonus_test_case_that_might_make/