import itertools

calibration_equations = open("input.txt").read().split("\n")

def solve(equations):
    part1 = 0
    for equation in equations:
        testValue, remaining_nums = equation.split(":")
        nums = [*map(int, remaining_nums.strip().split(" "))]
        # I dont want permutations, or permutations with replacement, but a Cartesian product
        ops_combos = itertools.product(["+", "*"], repeat=len(nums)-1)
        value = nums[0]
        for ops in ops_combos:
            for i in range(len(ops)):
                if ops[i] == "+":
                    value += nums[i+1]
                elif ops[i] == "*":
                    value *= nums[i+1]
            if value == int(testValue):
                part1 += int(testValue)
                break
            else:
                value = nums[0]
    return part1

# print(solve([
#     '292: 11 6 16 20'
# ]))
print(f"part 1: {solve(calibration_equations)}")
        