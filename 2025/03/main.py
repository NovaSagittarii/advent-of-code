import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

ans = 0
for line in lines:
    best = 0
    n = len(line)
    for i in range(n):
        for j in range(i+1, n):
            best = max(best, int(line[i] + line[j]))
    ans += best
print(ans)
