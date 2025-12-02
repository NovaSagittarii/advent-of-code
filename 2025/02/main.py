import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

ranges = ("".join(lines)).split(',')
ans = 0
for lr in ranges:
    l, r = map(int, lr.split('-'))
    for x in range(l, r+1):
        x = str(x)
        for k in range(2, len(x)+1):
            if len(x) % k == 0:
                h = len(x) // k
                if x == (x[:h] * k):
                    ans += int(x)
                    # print(x)
                    break
print(ans)

