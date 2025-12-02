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
        h = len(x)//2
        if len(x)%2 == 0 and x[:h] == x[h:]:
            ans += int(x)
print(ans)

