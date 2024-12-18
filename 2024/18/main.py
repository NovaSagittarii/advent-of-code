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
    A.append(arrayint(line.split(',')))

n = 71
T = len(A)

def doesitwork(W):
    a = [[0 for i in range(n)] for j in range(n)]
    for t, xy in enumerate(A[:W]):
        x, y = xy
        a[y][x] = 1

    # for row in a: print(*row)

    q = [(0, 0, 0)]
    ans = 0
    vis = set()
    while len(q):
        nq = []
        ok = False
        for t, i, j in q:
            if a[i][j]: continue
            # print(i, j, t, a[i][j])
            k = (i, j)
            if k in vis: continue
            vis.add(k)
            if i == n-1 and j == n-1:
                return t
            for di, dj in DIR:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    nq.append((t+1, ni, nj))
        if ok: break
        q = nq
    return -1

print(doesitwork(1024))
lo = 0
hi = T
lmid = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if doesitwork(mid) >= 0:
        lo = mid + 1
        lmid = mid
    else:
        hi = mid - 1
print(A[lmid])
