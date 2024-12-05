import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

A = []
rule = []
for line in lines:
    # A.append(arrayint(line.split()))
    if not line: continue
    if "|" in line:
        rule.append(arrayint(line.split('|')))
    else:
        A.append(arrayint(line.split(',')))

tot = 0
tot2 = 0
for a in A:
    ok = True
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            for u, v in rule:
                if a[i] == v and a[j] == u:
                    ok = False
                    a[i] = u
                    a[j] = v
    if ok:
        # print(a, a[n//2])
        tot += a[n//2]
    else:
        # print(a, a[n//2])
        tot2 += a[n//2]
print(tot)
print(tot2)
