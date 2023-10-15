import ast

packets = list(map(lambda pair: list(map(ast.literal_eval, pair.split("\n"))), open("input.txt", encoding="UTF-8").read().rstrip().split("\n\n")))

def check_order(left, right, index = 0) -> bool:
    # print(" " * index + f"- Compare {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int): # base case
        if left > right:
            # print(" " * index + f"- Right side is smaller, so the inputs are not in the right order")
            return False
        elif left < right:
            # print(" " * index + f"- Left side is smaller, so the inputs are in the right order")
            return True
        # do nothing aka "continue"
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if len(right) <= i:
                # print(" " * index + f"- Right side ran out of items, so inputs are not in the right order")
                return False
            outcome = check_order(left[i], right[i], index+1)
            if isinstance(outcome, bool):
                return outcome
        ## print(" " * index + f"- Left side ran out of items, so inputs are in the right order")
        return check_order(len(left), len(right))
    elif isinstance(left, int) and not isinstance(right, int):
        # print(" " * index + f"- Mixed types; convert left to {[left]} and retry comparison")
        return check_order([left], right, index+1)
    elif not isinstance(left, int) and isinstance(right, int):
        # print(" " * index + f"- Mixed types; convert right to {[right]} and retry comparison")
        return check_order(left, [right], index+1)
    # general case
    # do nothing aka "continue"

sum_of_indexs = 0
for (i, pair) in enumerate(packets):
    # print(f"== Pair {i + 1} ==")
    if check_order(pair[0], pair[1]):
        # print(f"pair: {i + 1}")
        sum_of_indexs+=i+1
print(f"part 1: {sum_of_indexs}")

flatten = [item for row in packets for item in row]
flatten.append([[2]])
flatten.append([[6]])
# print(flatten)
for (i, left) in enumerate(flatten):
    for (j, right) in enumerate(flatten):
        if i == j:
            continue
        # switch the j, and i thing to switch the order
        if not check_order(flatten[j], flatten[i]):
            # commenting and uncommenting the other line has no effect
            # flatten[j], flatten[i] = flatten[i], flatten[j]
            flatten[i], flatten[j] = flatten[j], flatten[i]


# print("\n".join(list(map(lambda s: json.dumps(s), flatten))))
first_divider_key = flatten.index([[2]]) + 1
second_divider_key = flatten.index([[6]]) + 1
print(f"part 2: {first_divider_key * second_divider_key}")
