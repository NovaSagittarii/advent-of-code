import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

lines = [arrayint(list(line)) for line in lines]
n = len(lines)
m = len(lines[0])

"""
  3
  ^
2< > 0
  v
  1
"""
DIR = ((0,1), (1,0), (0,-1), (-1,0))

vis = [[[[False for _r in range(4)] for _d in range(4)] for _j in line] for line in lines]
# cost, i, j, curdir, remaining
import heapq
pq = []
def insert(c, i, j, dir, remaining):
    di, dj = DIR[dir]
    ni = i + di
    nj = j + dj
    if 0 <= ni < n and 0 <= nj < m:
        heapq.heappush(pq, (c+lines[ni][nj], ni, nj, dir, remaining-1))
for i in range(3): insert(0, 0, 0, i, 3)

while len(pq):
    cost, i, j, curdir, remaining = heapq.heappop(pq)
    # go straight?
    if vis[i][j][curdir][remaining]: continue
    if i == n-1 and j == m-1:
        print(cost)
        break
    vis[i][j][curdir][remaining] = True
    if remaining > 0:
        insert(cost, i, j, curdir, remaining)
    # turn left/right
    insert(cost, i, j, (curdir-1)%4, 3)
    insert(cost, i, j, (curdir+1)%4, 3)

# for line in vis:
#     print("".join('#' if x else '.' for x in line))