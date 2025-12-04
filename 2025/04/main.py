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
    A.append(list('.' + line + '.'))
m = len(A[0])
w = list('.' * m)
A = [w] + A + [w]
n = len(A)

# for x in A: print(*x)
ans = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        if A[i][j] != '@': continue
        ct = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if not di and not dj: continue
                ni = i + di
                nj = j + dj
                if A[ni][nj] == '@':
                    ct += 1
        if ct < 4:
            ans += 1
print(ans)
