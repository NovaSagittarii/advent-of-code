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

MAXCONSEC = 10
vis = [[[[False for _r in range(MAXCONSEC+1)] for _d in range(4)] for _j in line] for line in lines]
# cost, i, j, curdir, consec
import heapq
pq = []
def insert(c, i, j, dir, consec):
    di, dj = DIR[dir]
    ni = i + di
    nj = j + dj
    if 0 <= ni < n and 0 <= nj < m:
        heapq.heappush(pq, (c+lines[ni][nj], ni, nj, dir, consec+1))
for i in range(4): insert(0, 0, 0, i, 0)

while len(pq):
    cost, i, j, curdir, consec = heapq.heappop(pq)
    # go straight?
    if vis[i][j][curdir][consec]: continue
    if i == n-1 and j == m-1:
        print(cost)
        break
    vis[i][j][curdir][consec] = True
    if consec < 10:
        insert(cost, i, j, curdir, consec)
    # turn left/right
    if consec >= 4:
        insert(cost, i, j, (curdir-1)%4, 0)
        insert(cost, i, j, (curdir+1)%4, 0)

# for line in vis:
#     print("".join('#' if x else '.' for x in line))