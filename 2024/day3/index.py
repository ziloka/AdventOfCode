import re
input = open("input.txt", "r").read()
def part1():
    mul_instructions = re.findall("mul\((\d{1,3}),(\d{1,3})\)", input)
    summation = 0
    for instru in mul_instructions:
        n1, n2 = [*map(int, instru)]
        summation += (n1 * n2)
    return summation
print(f"part 1: {part1()}")
# (mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)
instructions = re.findall("(mul)\((\d{1,3}),(\d{1,3})\)|(do|don't)\(\)", input)
instructions = [[*filter(lambda s: s != "", list(instr))] for instr in instructions]

summation = 0
should_execute = True
for inst in instructions:
    match inst[0]:
        case "mul":
            if should_execute:
                n1, n2 = [*map(int, inst[1:])]
                summation += (n1 * n2)
        case "do":
            should_execute = True
        case "don't":
            should_execute = False
print(f"part 2: {summation}")