import functools

individual_blocks = []
diskmap = [*map(int, [*open("example.txt").read()])]
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
        last_space = i

space_idx = 0
files_idx = len(files) - 1
while space_idx < len(spaces):
    s = spaces[space_idx]
    f, fileId = files[files_idx]
    print("".join(individual_blocks))
    individual_blocks[s] = fileId
    individual_blocks[f] = "."
    space_idx += 1
    files_idx -= 1
    print(space_idx, spaces[space_idx:])

checksum = 0
for i, d in enumerate([*filter(lambda s: s != '.', individual_blocks)]):
    checksum += int(d) * i
print(f"part 1: {checksum}")