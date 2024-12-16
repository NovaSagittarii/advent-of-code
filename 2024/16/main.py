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
sd = 0
for i in range(n):
    for j in range(m):
        if A[i][j] == 'S':
            heapq.heappush(pq, (0, i, j, 0))
            si, sj = i, j
        if A[i][j] == 'E':
            ti, tj = i, j


td = -1
vis = {}
while len(pq):
    c, i, j, d = heapq.heappop(pq)
    k = (i, j, d)
    if k in vis: continue
    vis[k] = c
    if A[i][j] == 'E' and td == -1:
        td = d
        print(c)
    # A[i][j] = '-'
    di, dj = DIR[d]
    ni = i - di
    nj = j - dj
    if A[ni][nj] != '#':
        heapq.heappush(pq, (c + 1, ni, nj, d))
    heapq.heappush(pq, (c + 1000, i, j, (d+1) % 4))
    heapq.heappush(pq, (c + 1000, i, j, (d-1+4) % 4))

vis2 = {}
pq = [(0, ti, tj, d) for d in range(4)]
heapq.heapify(pq)
while len(pq):
    c, i, j, d = heapq.heappop(pq)
    k = (i, j, d)
    if k in vis2: continue
    vis2[k] = c
    # if A[i][j] == 'S' and d == 0:
    #     continue
    di, dj = DIR[d]
    ni = i + di
    nj = j + dj
    if A[ni][nj] != '#':
        heapq.heappush(pq, (c + 1, ni, nj, d))
    heapq.heappush(pq, (c + 1000, i, j, (d+1) % 4))
    heapq.heappush(pq, (c + 1000, i, j, (d-1+4) % 4))

best = vis[(ti, tj, td)]
ans = 0
for i in range(n):
    for j in range(m):
        for d in range(4):
            k = (i, j, d)
            if A[i][j] == '#': continue
            # if k not in vis: continue
            # if k not in vis2: continue
            u = vis[k]
            v = vis2[k]
            # print(k, u+v)
            if u + v == best:
                ans += 1
                A[i][j] = 'O'
                break
print(ans)
# for row in A: print(*row)
