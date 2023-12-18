import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

"""
  3
  ^
2< > 0
  v
  1
"""
DIR = ((0,1), (1,0), (0,-1), (-1,0))
DIRX = {
    "R": 0,
    "D": 1,
    "L": 2,
    "U": 3,
}
n = 1000
m = 1000
vis = [[False for j in range(m)] for i in range(n)]

# mini, minj = 0, 0
# maxi, maxj = 0, 0
i, j = 500, 500
for line in lines:
    d, x, c = line.split()
    x = int(x)
    for t in range(x):
        di, dj = DIR[DIRX[d]]
        vis[i][j] = True
        i += di
        j += dj
#         mini = min(mini, i)
#         minj = min(minj, j)
#         maxi = max(maxi, i)
#         maxj = max(maxj, j)
# print(mini, maxi, minj, maxj)
# for line in vis:
#     print("".join(['#' if x else '.' for x in line]))

q = [(501, 501)]
while len(q):
    nq = []
    for i, j in q:
        if vis[i][j]: continue
        vis[i][j] = True
        for di, dj in DIR:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m:
                nq.append((ni, nj))
    q = nq
ans = 0
for i in range(n):
    for j in range(m):
        ans += 1 if vis[i][j] else 0
print(ans)