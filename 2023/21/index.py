import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

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

ok = False
for i in range(n):
    for j in range(m):
        if lines[i][j] == 'S':
            si = i
            sj = j
            ok = True
            break
    if ok: break

import functools
@functools.cache
def future(si, sj):
    vis = [[-1 for j in range(m)] for i in range(n)]
    q = [(si, sj)]
    # fails if the edge is not easily accessible (true in these tests at least tho lol)
    far_enough = max(n, m) * 4
    acc = [-1 for i in range(far_enough)]
    for t in range(far_enough):
        acc[t] = 0
        nq = []
        if t >= 2: acc[t] += acc[t-2]
        for i, j in q:
            if lines[i][j] == '#': continue
            if vis[i][j] != -1: continue
            vis[i][j] = t
            acc[t] += 1
            for d, dij in enumerate(DIR):
                di, dj = dij
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    nq.append((ni, nj))
        q = nq
        if t > 10 and acc[t] == acc[t-2] and acc[t-1] == acc[t-3]:
            acc = tuple(x for x in acc if x >= 0)
            break
    # for line in vis:
    #     print("\t".join(str(x) for x in line))
    return acc

def query(si, sj, steps):
    if steps == 0: return 1
    elif steps < 0: return 0
    ans = 0
    acc = future(si, sj)
    # print(border_cost, border_loc)
    # how much can you reach in this subgrid?
    # print(steps-cost)
    steps_allowed = steps
    if steps_allowed < len(acc):
        # in calculated grid
        ans += acc[steps_allowed]
        # print('+', acc[steps_allowed])
    else: # you can go wAYYYY off
        if (len(acc)-1) % 2 == (steps_allowed % 2):
            # which parity to take
            ans += acc[-1]
            # print('+', acc[-1])
        else:
            ans += acc[-2]
            # print('+', acc[-2])
    return ans

for k in (7, 14, 21, 35, 1000, 5000, 101365, 26501365):
    # if k > 100: break
    # the center!
    ans = query(si, sj, k)

    # straight movements
    cost = k - (si + 1)
    while cost >= 0:
        ans += query(0, sj, cost)
        ans += query(n-1, sj, cost)
        ans += query(si, 0, cost)
        ans += query(si, m-1, cost)
        cost -= n # move from one edge to the next
        
    # corner zone
    dup = 1
    cost = k - 2 * (si + 1)
    while cost >= 0:
        ans_batch = query(0, 0, cost)
        ans_batch += query(0, m-1, cost)
        ans_batch += query(n-1, 0, cost)
        ans_batch += query(n-1, m-1, cost)
        ans += ans_batch * dup
        dup += 1
        cost -= n # move from one corner to the next
    print(f"k={k} ans={ans}")