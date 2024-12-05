puzzle_input = open("input.txt").read()
page_ordering_rules, pages_to_produce = puzzle_input.split("\n\n")
page_ordering_rules = [*map(lambda s: [*map(int, s.split("|"))], page_ordering_rules.split("\n"))]
updates = [*map(lambda s: [*map(int, s.split(","))], pages_to_produce.split("\n"))]

sum_middle_pages = 0
for page_nums in updates:
    valid = True
    for num in page_nums:
        for rules in page_ordering_rules:
            if num in rules and rules[0] in page_nums and rules[1] in page_nums:
                first = page_nums.index(rules[0])
                second = page_nums.index(rules[1])
                if first > second:
                    valid = False
                    break
    if valid:
        sum_middle_pages += page_nums[len(page_nums) // 2]

print(f"part 1: {sum_middle_pages}")