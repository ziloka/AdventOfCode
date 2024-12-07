import time
import itertools

def part1(equations):
    total_calibration_result = 0
    for equation in equations:
        testValue, remaining_nums = equation.split(":")
        nums = [*map(int, remaining_nums.strip().split(" "))]
        # I dont want permutations, or permutations with replacement, but a Cartesian product
        ops_combos = itertools.product(["+", "*"], repeat=len(nums)-1)
        result = nums[0]
        for ops in ops_combos:
            for i in range(len(ops)):
                if ops[i] == "+":
                    result += nums[i+1]
                elif ops[i] == "*":
                    result *= nums[i+1]
            if result == int(testValue):
                total_calibration_result += int(testValue)
                break
            else:
                result = nums[0]
    return total_calibration_result

def part2_helper(nums, ops, expectedValue):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            result += nums[i+1]
        elif ops[i] == "*":
            result *= nums[i+1]
        elif ops[i] == "||":
            result = int(str(result) + str(nums[i+1]))

        # improve code perf
        if result > int(expectedValue):
            return False

    return result == int(expectedValue)

def part2(equations):
    total_calibration_result = 0
    for equation in equations:
        testValue, remaining_nums = equation.split(":")
        nums = [*map(int, remaining_nums.strip().split(" "))]
        # I dont want permutations, or permutations with replacement, but a Cartesian product
        ops_combos = itertools.product(["+", "*", "||"], repeat=len(nums)-1)
        for ops in ops_combos:
            if part2_helper(nums, ops, int(testValue)):
                total_calibration_result += int(testValue)
                break
    return total_calibration_result

calibration_equations = open("input.txt").read().split("\n")
start = time.time()
print(f"part 1: {part1(calibration_equations)}")
print(f"part 2: {part2(calibration_equations)}")
print(f"took {time.time() - start:.2f}s")