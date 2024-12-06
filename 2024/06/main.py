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
    A.append(list(line))

n = len(A)
m = len(A[0])
xi, xj = 0, 0
for i in range(n):
    for j in range(m):
        if A[i][j] == '^':
            xi, xj = i, j
xd = 3

vis = set()
while True:
    k = (xi, xj, xd)
    if k in vis: break
    vis.add(k)
    A[xi][xj] = 'X'
    di, dj = DIR[xd]
    ni = xi + di
    nj = xj + dj
    while 0 <= ni < n and 0 <= nj < m and A[ni][nj] == '#':
        xd = (xd + 1) % 4
        di, dj = DIR[xd]
        ni = xi + di
        nj = xj + dj

        k = (xi, xj, xd)
        if k in vis: break
        vis.add(k)
    if 0 <= ni < n and 0 <= nj < m and A[ni][nj] != '#':
        xi = ni
        xj = nj
    else: break # looped!

tot = 0
for l in A:
    tot += len([c for c in l if c == 'X'])
print(tot)
