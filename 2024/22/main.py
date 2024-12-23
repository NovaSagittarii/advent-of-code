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
    A.append(int(line))

ans = {}
def sec(x):
    global ans
    vis = set()
    mem = [-10, -10, -10, -10, x % 10]
    for _ in range(2000):
        x ^= (x<<6)
        x &= 16777215
        x ^= (x>>5)
        x &= 16777215
        x ^= (x<<11)
        x &= 16777215
        mem[0] = mem[1]
        mem[1] = mem[2]
        mem[2] = mem[3]
        mem[3] = mem[4]
        mem[4] = x % 10
        if mem[0] == -10: continue
        k = tuple(mem[i+1] - mem[i] for i in range(4))
        if k in vis: continue
        vis.add(k)
        if k not in ans: ans[k] = 0
        ans[k] += x % 10
    
for x in A:
    sec(x)
# print(ans)
print(max(ans.values()))