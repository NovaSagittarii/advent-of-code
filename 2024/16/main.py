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

import heapq

n = len(A)
m = len(A[0])
pq = []
for i in range(n):
    for j in range(m):
        if A[i][j] == 'S':
            heapq.heappush(pq, (0, i, j, 0))

vis = set()
while len(pq):
    c, i, j, d = heapq.heappop(pq)
    k = (i, j, d)
    if k in vis: continue
    vis.add(k)
    if A[i][j] == 'E':
        print(c)
        break
    A[i][j] = '-'
    di, dj = DIR[d]
    ni = i + di
    nj = j + dj
    if A[ni][nj] != '#':
        heapq.heappush(pq, (c + 1, ni, nj, d))
    heapq.heappush(pq, (c + 1000, i, j, (d+1) % 4))
    heapq.heappush(pq, (c + 1000, i, j, (d-1+4) % 4))

# for w in A: print(*w)