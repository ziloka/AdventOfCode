# chatgpt's "fork bomb" (it would be a good solution if the computer had 10^5 gb's of RAM)

import time
from functools import lru_cache

def parse_input(input_text):
    equations = []
    for line in input_text.strip().split("\n"):
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        equations.append((target, numbers))
    return equations

@lru_cache(None)
def evaluate_expression(target, numbers):
    if len(numbers) == 1:  # Base case: only one number
        return numbers[0] == target

    for i in range(1, len(numbers)):
        left, right = numbers[:i], numbers[i:]
        
        # Evaluate all possible operations between left and right
        left_values = possible_values(left)
        right_values = possible_values(right)
        
        for lv in left_values:
            for rv in right_values:
                # Try addition
                if lv + rv == target:
                    return True
                # Try multiplication
                if lv * rv == target:
                    return True
                # Try concatenation
                if int(str(lv) + str(rv)) == target:
                    return True
    return False

def possible_values(numbers):
    """Generate all possible values from a list of numbers."""
    if len(numbers) == 1:
        return {numbers[0]}
    
    results = set()
    for i in range(1, len(numbers)):
        left, right = numbers[:i], numbers[i:]
        
        left_values = possible_values(left)
        right_values = possible_values(right)
        
        for lv in left_values:
            for rv in right_values:
                # Add all possible results of operations
                results.add(lv + rv)
                results.add(lv * rv)
                results.add(int(str(lv) + str(rv)))
    return results

def calculate_total_calibration(input_text):
    equations = parse_input(input_text)
    total = 0
    for target, numbers in equations:
        if evaluate_expression(target, tuple(numbers)):
            total += target
    return total

# Example usage
start_time = time.time()
input_text = open("input.txt").read()
print(calculate_total_calibration(input_text))
print(f"took {time.time() - start_time:.2f}s")