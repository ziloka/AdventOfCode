# 3 cols
# 2 rows
# i (1, 2, 3, 4, 5, 6)

# 1 2 3
# 4 5 6

# [0, 2] = 3, (3 % cols, 3 // rows)
# [1, 2] = 5, (5 % cols, // rows)

table = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

def get_coords(cols, i):
    return (i // cols, i % cols)

print(get_coords(5, 8))