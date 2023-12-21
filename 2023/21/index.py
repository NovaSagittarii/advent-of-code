import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

n = len(lines)
m = len(lines[0])
vis = [[-1 for j in range(m)] for i in range(n)]

"""
  3
  ^
2< > 0
  v
  1
"""
DIR = ((0,1), (1,0), (0,-1), (-1,0))

q = []
ok = False
for i in range(n):
    for j in range(m):
        if lines[i][j] == 'S':
            q.append((i, j))
            ok = True
            break
    if ok: break

acc = [0 for i in range(100)]
for t in range(0, 65):
    nq = []
    for i, j in q:
        if lines[i][j] == '#': continue
        if vis[i][j] == t: continue
        vis[i][j] = t
        acc[t] += 1
        for di, dj in DIR:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m:
                nq.append((ni, nj))
    q = nq
print(acc[64])