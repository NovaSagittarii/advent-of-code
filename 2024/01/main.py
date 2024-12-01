import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

a = []
b = []
for line in lines:
    x, y = arrayint(line.split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()

tot = 0
for i, x in enumerate(a):
    y = b[i]
    tot += abs(x-y)
print(tot)