def parse(filename):
    puzzle_input = open(filename).read()
    page_ordering_rules, pages_to_produce = puzzle_input.split("\n\n")
    page_ordering_rules = [*map(lambda s: [*map(int, s.split("|"))], page_ordering_rules.split("\n"))]
    updates = [*map(lambda s: [*map(int, s.split(","))], pages_to_produce.split("\n"))]
    return page_ordering_rules, updates

def is_valid(page_ordering_rules, page_nums):
    valid = True
    for num in page_nums:
        for rules in page_ordering_rules:
            if num in rules and rules[0] in page_nums and rules[1] in page_nums:
                first = page_nums.index(rules[0])
                second = page_nums.index(rules[1])
                if first > second:
                    valid = False
                    break
    return valid

def part1(page_ordering_rules, updates):
    sum_middle_pages = 0
    for page_nums in updates:
        if is_valid(page_ordering_rules, page_nums):
            sum_middle_pages += page_nums[len(page_nums) // 2]
    return sum_middle_pages

def fix_page_nums(page_ordering_rules, page_nums):
    for i in range(len(page_nums)):
        for rules in page_ordering_rules:
            # perform selection sort, figure out first position, then second position, and so forth
            if page_nums[i] in rules and rules[0] in page_nums and rules[1] in page_nums:
                first = page_nums.index(rules[0])
                second = page_nums.index(rules[1])
                if first > second:
                    page_nums[second], page_nums[first] = page_nums[first], page_nums[second]
    return page_nums

def part2(page_ordering_rules, updates):
    sum_middle_pages = 0
    for page_nums in updates:
        if not is_valid(page_ordering_rules, page_nums):
            page_nums = fix_page_nums(page_ordering_rules, page_nums)
        sum_middle_pages += page_nums[len(page_nums) // 2]
    return sum_middle_pages

args = parse("input.txt")
print(f"part 1: {part1(*args)}")
print(f"part 2: {part2(*args)}") # 11666 is too high