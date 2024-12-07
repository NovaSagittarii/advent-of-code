import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

A = []
for line in lines:
    l, r = line.split(':')
    A.append((int(l), arrayint(r.split())))

tot = 0
for k, a in A:
    dp = [a[0]]
    for x in a[1:]:
        ndp = []
        for w in dp:
            ndp.append(w + x)
            ndp.append(w * x)
        dp = set(ndp)
    if k in dp:
        tot += k
print(tot)



