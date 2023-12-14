import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

n = len(lines)
m = len(lines[0])
lines = [list(line) for line in lines]

vis = {}

DIRECTION = ((-1,0),(0,-1),(1,0),(0,1))
t = 0
TMAX = 1000000000
while t < TMAX:
    t += 1
    k = tuple("".join(line) for line in lines)
    if k in vis:
        cycle = (vis[k] - t)
        step = (TMAX - t - 100) // cycle
        t += step * cycle
        if step > 0:
            print("skip ", step*cycle)
            continue
        # if step > 0: continue
    else: vis[k] = t
    
    RN = tuple(range(n))
    RM = tuple(range(m))
    RNr = tuple(range(n))[::-1]
    RMr = tuple(range(m))[::-1]
    DIRS = ((-1,0,RN,RM),
            (0,-1,RN,RM),
            (1,0,RNr,RMr),
            (0,1,RNr,RMr))
    for di, dj, RN, RM in DIRS:
        for ts in range(max(n, m)):
            change = False
            for i in RN:
                for j in RM:
                    if lines[i][j] == 'O':
                        ni = i+di
                        nj = j+dj
                        if 0 <= ni < n and 0 <= nj < m:
                            if lines[ni][nj] == '.':
                                lines[ni][nj] = 'O'
                                lines[i][j] = '.'
                                change = True
            if not change: break
    
    # print(t)
    # for line in lines:print("".join(line))
    # print()
    

ans = 0
for i, line in enumerate(lines):
    for c in line:
        if c == 'O':
            ans += (n-i)
print(ans)