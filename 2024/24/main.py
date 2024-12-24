import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

dp = {}
defs = {}
for line in lines:
    if ':' in line:
        k, v = line.split(': ')
        v = int(v)
        dp[k] = v
    elif '->' in line:
        xy, z = line.split(' -> ')
        defs[z] = tuple(xy.split())
def dfs(u):
    if u in dp: return dp[u]
    x, op, y = defs[u]
    x = dfs(x)
    y = dfs(y)
    if op == 'OR': ret = x | y
    elif op == 'AND': ret = x & y
    elif op == 'XOR': ret = x ^ y
    dp[u] = ret
    return ret

for u in defs.keys(): dfs(u)
ans = ""
for u in sorted(defs.keys(), reverse=True):
    if u[0] == 'z':
        # print(u, dfs(u))
        ans += str(dfs(u))
print(int(ans, 2))