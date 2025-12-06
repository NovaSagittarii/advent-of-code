import math
import re
import sys
lines = [line for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

A = []
for line in lines:
    A.append(line.split())

ans = 0
n = len(A)
m = len(A[0])
for j in range(m):
    op = A[-1][j]
    tot = 0
    if op == '*': tot = 1
    a = []
    for i in range(n-1):
        x = int(A[i][j])
        a.append(x)
    b = []
    
    for x in a:
        if op == '*': tot *= x
        else: tot += x
    ans += tot
print(ans)

ans2 = 0
n = len(lines)
idx = [i for i, x in enumerate(lines[-1]+'$') if x != ' ']
for l, r in zip(idx[:-1], idx[1:]):
    op = lines[-1][l]
    tot = 0
    if op == '*': tot = 1
    a = []
    for j in range(l, r):
        s = ""
        for i in range(n-1):
            s += lines[i][j]
        if s.strip(): a.append(int(s))
    for x in a:
        if op == '*': tot *= x
        else: tot += x
    ans2 += tot
print(ans2)
