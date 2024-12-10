def parse_disk_map(disk_map):
    individual_blocks = []
    files = []
    spaces = []
    
    for i, digit in enumerate(disk_map):
        length = int(digit)
        if i % 2 == 0:  # Even index -> File length
            file_id = len(files)  # Unique file ID based on its order
            files.append((file_id, length))
            individual_blocks.extend([str(file_id)] * length)
        else:  # Odd index -> Space length
            spaces.append((len(individual_blocks), length))
            individual_blocks.extend(['.'] * length)
    
    return individual_blocks, spaces, files

def move_files(individual_blocks, spaces, files):
    # Move files in reverse order (highest ID first)
    for file_id, file_size in reversed(files):
        original_position = individual_blocks.index(str(file_id))
        best_start = None
        
        # Find the leftmost available space that can fit the file
        for space_start, space_size in spaces:
            if space_start < original_position and space_size >= file_size:
                best_start = space_start
                break  # We take the first suitable space

        # Move the file if a suitable space is found
        if best_start is not None:
            # Clear the original position of the file
            for i in range(original_position, original_position + file_size):
                individual_blocks[i] = '.'

            # Move the file to the found space
            for i in range(best_start, best_start + file_size):
                individual_blocks[i] = str(file_id)

            # Update the spaces list
            for index in range(len(spaces)):
                if spaces[index][0] == best_start:
                    new_start = spaces[index][0] + file_size
                    new_size = spaces[index][1] - file_size
                    spaces[index] = (new_start, new_size)
                    break

def calculate_checksum(individual_blocks):
    checksum = 0
    for i, block in enumerate(individual_blocks):
        if block != '.':
            checksum += int(block) * i  # Only sum for blocks with file IDs
    return checksum

def compact_disk(disk_map):
    individual_blocks, spaces, files = parse_disk_map(disk_map)
    move_files(individual_blocks, spaces, files)
    return calculate_checksum(individual_blocks)

# Example usage
disk_map = open("input.txt").read()  # Example disk map input
resulting_checksum = compact_disk(disk_map)
print(f"Resulting Checksum: {resulting_checksum}")  # Expected output: 2158
