import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

adj = {}
for line in lines:
    u, v = line.split('-')
    if u not in adj: adj[u] = []
    if v not in adj: adj[v] = []
    adj[u].append(v)
    adj[v].append(u)

tot = 0
vis = set()
for u in adj.keys(): # start
    # if u[0] != 't': continue
    for v in adj[u]: # 2nd
        for k in adj[v]: # third
            if k == u: continue
            for l in adj[k]: # Loop again?
                if l == v: continue
                if u == l:
                    tot += 1
                    vis.add(tuple(sorted([u, v, k])))
# print(vis)
print(len(vis))

# co, de, ka, and ta.

best = []
def dfs(prev): # maximal clique search
    u = prev[-1]
    global best
    if len(prev) > len(best):
        best.clear()
        for u in prev: best.append(u)
        print(",".join(sorted(best)))
        # best = prev # this doesnt work???
    for v in adj[u]:
        if v in prev: continue
        ok = True
        for req in prev:
            if req not in adj[v]:
                ok = False
                break
        if ok:
            prev.append(v)
            dfs(prev)
            prev.pop()
for i, tri in enumerate(vis):
    print(f"{i} of {len(vis)}")
    t1, t2, t3 = tri
    # suppose t1 t2 t3 are in a clique
    dfs([t1, t2, t3])
    dfs([t2, t3, t1])
    dfs([t3, t1, t2])
print(",".join(sorted(best)))
