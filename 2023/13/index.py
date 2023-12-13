import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

grids = ("\n".join(lines)).split("\n\n")

ans = 0
for grid in grids:
    grid = grid.split("\n")
    n = len(grid)
    m = len(grid[0])
    w = -1
    # vertical
    for t in range(0, n-1):
        k = t+0.5
        ok = 2
        for i in range(t+1):
            ni = int(k + (k-i))
            for j in range(m):
                if 0 <= ni < n:
                    if grid[i][j] != grid[ni][j]:
                        ok -= 1
        if ok == 1:
            w = t+1
            w *= 100
            break
    # horizontal
    if w == -1:
        for t in range(0, m-1):
            k = t+0.5
            ok = 2
            for j in range(t+1):
                nj = int(k + (k-j))
                for i in range(n):
                    if 0 <= nj < m:
                        if grid[i][j] != grid[i][nj]:
                            ok -= 1
            if ok == 1:
                w = t+1
                break
    # print('#', n, m)
    # print(grid)
    print(w)
    ans += w
print(ans)