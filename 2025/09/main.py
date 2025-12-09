import math
import re
import sys

lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

a = []
for line in lines:
    a.append(tuple(map(int, line.split(","))))
n = len(a)

ans = 0
for x, y in a:
    for x2, y2 in a:
        w = (x - x2 + 1) * (y - y2 + 1)
        ans = max(ans, abs(w))
        # print(abs(w), x, y, x2, y2)
print(ans)
