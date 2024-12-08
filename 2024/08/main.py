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

n = len(A)
m = len(A[0])
a = {}
for i in range(n):
    for j in range(m):
        c = A[i][j]
        if c == '.': continue
        if c not in a: a[c] = []
        a[c].append((i, j))

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
def is_collinear(x1, y1, x2, y2, x3, y3):
    return (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) == 0

tot = 0
for i in range(n):
    for j in range(m):
        ok = False
        for k, v in a.items():
            sz = len(v)
            for p in range(sz):
                px, py = v[p]
                pd = dist(i, j, px, py)
                # if pd == 0: continue
                for q in range(p+1, sz):
                    qx, qy = v[q]
                    qd = dist(i, j, qx, qy)
                    # if qd == 0: continue
                    if not is_collinear(i, j, px, py, qx, qy):
                        continue
                    if True: # pd == 2*qd or 2*pd == qd:
                        # print(i, j, px, py, qx, qy, k)
                        # tot += 1
                        if not ok:
                            # A[i][j] += k
                            # A[i][j] = "#"
                            ok = True
                            break
                if ok: break
            if ok: break
        if ok: tot += 1
print(tot)

# for w in A: print(*w)