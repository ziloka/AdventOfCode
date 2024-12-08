# https://www.reddit.com/r/adventofcode/comments/1h8rzsp/comment/m0wcuvu/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

# Problem has an optimal substructure. Basically if there is a list of valid operations there has to be last operation. And bc of the left to right operation priority:
# The last operation can be multiplication if and only if the desired value is divisible by the last element
# The last operation can be concatenation if and only if the desired value ends with the digits of the last element.
# No conditions on additon. Edit, basic conditon on additon last value as to be strictly less than desired value.
# So you can recursively work backwards and the two checks will drastically reduce the ultimate search space.

import time

def can_calibrate(target, numbers, part2):
    """
    Check if the target value can be reached using the list of numbers
    and operations +, *, ||, with left-to-right evaluation.
    """

    # Base case: If there's only one number, check if it equals the target.
    if len(numbers) == 1:
        return numbers[0] == target

    last = numbers[-1]
    remaining = numbers[:-1]

    # Check addition (last value must be strictly less than the target).
    if target > last:
        if can_calibrate(target - last, remaining, part2):
            return True

    # Check multiplication (target must be divisible by the last value).
    if last != 0 and target % last == 0:
        if can_calibrate(target // last, remaining, part2):
            return True

    # Check concatenation (target must end with the digits of the last value).
    str_target = str(target)
    str_last = str(last)
    if part2 and str_target.endswith(str_last):
        concat_target = int(str_target[:-len(str_last)] or '0')  # Handle empty string as 0.
        if can_calibrate(concat_target, remaining, part2):
            return True

    return False

def total_calibration_result(input_data, part2=False):
    """
    Compute the total calibration result by summing the targets
    that can be calibrated with their respective numbers.
    """
    total = 0

    for line in input_data.splitlines():
        if not line.strip():
            continue

        target, numbers = line.split(":")
        target = int(target)
        numbers = list(map(int, numbers.split()))

        if can_calibrate(target, numbers, part2):
            total += target

    return total

# Example input
input_data = open("input.txt").read()
start_time = time.time()
print(f"part 1: {total_calibration_result(input_data)}")
print(f"part 2: {total_calibration_result(input_data, True)}")
print(f"took {time.time() - start_time:.2f}s")