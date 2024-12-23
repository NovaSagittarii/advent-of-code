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
    if u[0] != 't': continue
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

