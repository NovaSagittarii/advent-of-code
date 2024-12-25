import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

keys = []
locks = []
for k in range(0, len(lines), 8):
    lo = [9 for _ in range(5)]
    hi = [0 for _ in range(5)]
    for i in range(7):
        for j, c in enumerate(lines[k+i]):
            if c == '#': lo[j] = min(lo[j], i)
            if c == '#': hi[j] = max(hi[j], i)
    if lines[k][0] == '#': # a lock
        locks.append(hi)
    else:
        keys.append(lo)

tot = 0
for key in keys:
    for lock in locks:
        ok = True
        for i in range(5):
            if key[i] <= lock[i]:
                ok = False
        if ok:
            tot += 1
            # print(key, lock)
print(tot)
