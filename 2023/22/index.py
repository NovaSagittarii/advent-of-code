import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

n = 10
m = 10
zmax = 350
grid = [[[-1 for k in range(zmax)] for j in range(m)] for i in range(n)]

sticks = []
for line in lines:
    A, B = (coord.split(',') for coord in line.split('~'))
    x1, y1, z1 = arrayint(A)
    x2, y2, z2 = arrayint(B)
    X = tuple((min(x1, x2), min(y1, y2), min(z1, z2)))
    Y = tuple((max(x1, x2), max(y1, y2), max(z1, z2)))
    sticks.append((X, Y))
sticks.sort(key=lambda x: x[0][2])

def stick_coords(stick):
    X, Y = stick
    x1, y1, z1 = X
    x2, y2, z2 = Y
    length = max(x2-x1, y2-y1, z2-z1)
    di = min(x2-x1, 1)
    dj = min(y2-y1, 1)
    dk = min(z2-z1, 1)
    for t in range(length+1):
        yield (x1, y1, z1)
        x1 += di
        y1 += dj
        z1 += dk
def stick_translate(stick, offset):
    return tuple(tuple(stick_endpoint[i] + offset[i] for i in range(3)) for stick_endpoint in stick)

can_remove = [True for i in sticks]
adj = [[] for i in sticks]
supports = [0 for i in sticks]
for stick_id, stick in enumerate(sticks):
    for dz in range(1000):
        on_floor = False
        can_fall = True
        resting_on = set()
        for i, j, k in stick_coords(stick_translate(stick, (0, 0, -dz-1))):
            if k < 0 or grid[i][j][k] >= 0:
                can_fall = False
                if k < 0: on_floor = True
                if grid[i][j][k] >= 0:
                    resting_on.add(grid[i][j][k])
        if not can_fall:
            # solidify
            for i, j, k in stick_coords(stick_translate(stick, (0, 0, -dz))):
                grid[i][j][k] = stick_id
            # STR = "ABCDEFGHIJ"
            # print(STR[stick_id], [STR[x] for x in resting_on])
            if len(resting_on) == 1:
                for other in resting_on:
                    can_remove[other] = False
            for other in resting_on:
                adj[other].append(stick_id)
                supports[stick_id] += 1
            if on_floor: supports[stick_id] += 42069
            break
ans = sum(1 if x else 0 for x in can_remove)
print(ans)

# STR = "ABCDEFGHIJ"
# for i, lst in enumerate(adj):
#     print(STR[i], [STR[i] for i in lst])
# print(supports)

def accessible(u):
    left = supports[::] # -1 denotes fallen
    def dfs(u): # check if fallen
        if left[u] != 0: return
        left[u] = -1
        for v in adj[u]: left[v] -= 1 # update
        # print(u, left)
        for v in adj[u]: dfs(v) # propagate
    left[u] = 0
    dfs(u)
    return sum(1 if x == -1 else 0 for x in left)

ans = 0
for i, safe in enumerate(can_remove):
    # print(i, safe, accessible(i))
    if not safe:
        ans += accessible(i)-1
print(ans)