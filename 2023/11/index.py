import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

n = len(lines)
m = len(lines[0])

emptyrow = [True for _ in lines]
emptycol = [True for _ in lines[0]]
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != '.':
            emptyrow[i] = False
            emptycol[j] = False

cost = [[1 for l in line] for line in lines]
K = 1000000

coords = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != '.':
            coords.append((i, j))
        if emptyrow[i] or emptycol[j]:
            cost[i][j] = K

ans = 0
import heapq
for si, sj in coords:
    vis = [[False for _ in line] for line in lines]
    pq = [(0, si, sj)]
    while len(pq):
        c, i, j = pq[0]
        # print(pq[0])
        heapq.heappop(pq)
        # print(i, j)
        if vis[i][j]: continue
        vis[i][j] = True
        if lines[i][j] != '.':
            ans += c
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni = i+di
            nj = j+dj
            if 0 <= ni < n and 0 <= nj < m:
                if not vis[ni][nj]:
                    heapq.heappush(pq, (c + cost[ni][nj], ni, nj))
ans //= 2
print(ans)
