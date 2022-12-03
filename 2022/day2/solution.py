# https://www.reddit.com/r/adventofcode/comments/zac2v2/comment/iylda9n/?utm_source=share&utm_medium=web2x&context=3

import time

start = time.process_time()
f = lambda x: ('  BXCYAZAXBYCZCXAYBZ'.index(x[0]+x[2]),
               '  BXCXAXAYBYCYCZAZBZ'.index(x[0]+x[2]))

print(*[sum(x)//2 for x in zip(*map(f, open('input.txt')))])
print('took {}ms'.format((time.process_time() - start) / 1000))