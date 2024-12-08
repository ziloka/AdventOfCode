# https://chatgpt.com/share/67552610-648c-8003-a717-eba5cd710149

import time

def parse_input(input_text):
    equations = []
    for line in input_text.strip().split("\n"):
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        equations.append((target, numbers))
    return equations

def can_produce_target(target, numbers):
    """
    Determines if the given numbers can produce the target value using +, *, ||.
    Avoids storing all possible combinations by using a stack for iterative traversal.
    """
    n = len(numbers)
    if n == 1:
        return numbers[0] == target

    stack = [(numbers[0], 1)]  # (current value, index in numbers)
    
    while stack:
        current, idx = stack.pop()
        
        if idx == n:
            if current == target:
                return True
            continue
        
        next_number = numbers[idx]
        
        # Addition
        if current + next_number <= target:  # Early pruning
            stack.append((current + next_number, idx + 1))
        
        # Multiplication
        if current * next_number <= target:  # Early pruning
            stack.append((current * next_number, idx + 1))
        
        # Concatenation
        concatenated = int(f"{current}{next_number}")
        if concatenated <= target:  # Early pruning
            stack.append((concatenated, idx + 1))
    
    return False

def calculate_total_calibration(input_text):
    equations = parse_input(input_text)
    total = 0
    for target, numbers in equations:
        if can_produce_target(target, numbers):
            total += target
    return total

# Example usage
input_text = open("input.txt").read()
start_time = time.time()
print(calculate_total_calibration(input_text))
print(f"took {time.time() - start_time:.2f}s")