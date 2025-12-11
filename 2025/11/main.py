import functools
import sys

lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

adj = {}
radj = {}
for line in lines:
    u, *other = line.split()
    u = u[:-1]
    adj[u] = other
    for v in other:
        if v not in radj.keys():
            radj[v] = []
        radj[v].append(u)
for u in adj.keys():
    if u not in radj.keys():
        radj[u] = []

vis = set()

@functools.lru_cache(maxsize=None)
def dfs(u, prev) -> int:
    # print(u)
    if u == "you":
        return 1
    ret = 0
    for v in radj[u]:
        if v == prev:
            continue  # needed?
        assert v not in vis, "LOOP??"
        vis.add(v)
        ret += dfs(v, u)
        vis.remove(v)
    return ret
print(dfs("out", None))
