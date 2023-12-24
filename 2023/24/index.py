import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

pts = []

for line in lines:
    p, v = [arrayint(x.split(', ')) for x in line.split(' @ ')]
    p[2] = v[2] = 0
    pts.append((p, v))

ans = 0
N = len(pts)
for i in range(N):
    # px, py, pz = pts[i][0]
    # pvx, pvy, pvz = pts[i][1]
    for j in range(i+1, N):
        # qx, qy, qz = pts[j][0]
        # qvx, qvy, qvz = pts[j][1]
        # well if they intersect, x's gotta be the same
        # px + T pvx = qx + T qvx
        # (px - qx)  = T qvx - T pvx
        # (px - qx)  = T (qvx - pvx)
        # Tx = (px - qx) / (qvx - pvx)
        # does it work with the other?
        r1, e1 = pts[i]
        r2, e2 = pts[j]
        if e1 == e2: continue # parallel
        
        # https://stackoverflow.com/a/1984823
        def cross(a, b):
            c = [a[1]*b[2] - a[2]*b[1],
                a[2]*b[0] - a[0]*b[2],
                a[0]*b[1] - a[1]*b[0]]
            return c

        def dot(a, b):
            return sum(a[k] * b[k] for k in range(3))

        # https://math.stackexchange.com/a/2217845
        n = cross(e1, e2)
        if max(*n) == 0 and min(*n) == 0: continue # parallel

        r1_r2 = tuple(r1[k] - r2[k] for k in range(3)) # r1 - r2
        r2_r1 = tuple(r2[k] - r1[k] for k in range(3)) # r2 - r1
        d = abs(dot(n, r1_r2)) / dot(n, n)

        t1 = dot(cross(e2, n), r2_r1) / dot(n, n)
        t2 = dot(cross(e1, n), r2_r1) / dot(n, n)
        if t1 < 0 or t2 < 0: continue # collision in past
        pos = tuple(r1[k] + e1[k]*t1 for k in range(3))
        # print(r1, r2, 'at', pos)
        LO = 200000000000000
        HI = 400000000000000
        if LO <= pos[0] <= HI and LO <= pos[1] <= HI:
            ans += 1
print(ans)
        