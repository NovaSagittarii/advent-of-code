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
    aok = False
    for S in range(n+1): # what you wanna replace
        def f(x):
            if x >= S: return x+1
            else: return x
        diffs = []
        adiffs = []
        for i in range(n-1):
            if f(i+1) >= n: continue
            diffs.append(a[f(i+1)]-a[f(i)])
            adiffs.append(abs(a[f(i+1)]-a[f(i)]))
        ok = False
        if min(diffs) > 0 and max(diffs) > 0: ok = True
        if min(diffs) < 0 and max(diffs) < 0: ok = True
        if ok:
            if min(adiffs) >= 1 and max(adiffs) <= 3:
                ok = True
            else:
                ok = False
        if ok: 
            aok = True
    if aok: tot += 1
print(tot)
