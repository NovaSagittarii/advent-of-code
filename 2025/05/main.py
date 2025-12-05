import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

A = []
done1 = False
B = []
for line in lines:
    if not line:
        done1 = True
        continue
    if not done1: A.append(line)
    else: B.append(line)

ans = 0
for x in B:
    x = int(x)
    for a in A:
        l, r = map(int, a.split('-'))
        if l <= x <= r:
            ans += 1
            break
print(ans)

lrs = []
for a in A:
    l, r = map(int, a.split('-'))
    if l > r: print(f"{l}\n{r}\n")
    assert l <= r
    lrs.append((l, r+1))
lrs.sort()

ans2 = 0
last = 0
for l, r in lrs:
    l = max(l, last)
    last = max(last, r)
    # print(l, r)
    if r > l: ans2 += r - l
assert ans2 != 325650347334979 # err
print(ans2)