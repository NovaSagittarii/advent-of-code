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
    A.append(arrayint(line.split()))

tot = 0
for a in A:
    n = len(a)
    diffs = []
    adiffs = []
    for i in range(n-1):
        diffs.append(a[i+1]-a[i])
        adiffs.append(abs(a[i+1]-a[i]))
    ok = False
    if min(diffs) > 0 and max(diffs) > 0: ok = True
    if min(diffs) < 0 and max(diffs) < 0: ok = True
    if ok:
        if min(adiffs) >= 1 and max(adiffs) <= 3:
            ok = True
        else:
            ok = False
    if ok: 
        tot += 1
print(tot)
