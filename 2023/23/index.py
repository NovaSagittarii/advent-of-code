import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

sys.setrecursionlimit(1000000)

n = len(lines)
m = len(lines[0])
si = 0
sj = 1

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

bigi = 0
ans = 0
vis = [[False for j in range(m)] for i in range(n)]
def dfs(i, j, steps):
    # print(steps)
    # print(i, j)
    global ans
    # global bigi
    # if i > bigi:
    #     bigi = i
    #     print(bigi)
    if vis[i][j]: return
    vis[i][j] = True
    end = i == n-1
    if not end:
        for d, dij in enumerate(DIR):
            di, dj = dij
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m:
                c = lines[ni][nj]
                if c == '#': continue
                ok = True
                if c in SLOPE:
                    if SLOPE.index(c) != d: ok = False
                if ok:
                    dfs(ni, nj, steps + 1)
    vis[i][j] = False
    if end:
        # if ans > steps: print('!', ans)
        ans = max(ans, steps)
        # print(steps, ans)
        # for line in vis:
        #     print("".join('O' if x else '.' for x in line))
        # print()
    return

try:
    print(dfs(si, sj, 0))
    print(ans)
except Exception as e:
    print(e)