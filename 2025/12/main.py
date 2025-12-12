import math
import re
import sys

lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

*shapes, queries = ("\n".join(lines)).split("\n\n")

ans = 0
for q in queries.split("\n"):
    sz, *order = q.split()
    n, m = map(int, sz[:-1].split("x"))
    order = tuple(map(int, order))
    # print(n * m, sum(order) * 8)
    wei = [5, 7, 6, 8, 8, 7]  # hardcoded lol (how many # in a block)
    req = sum(x * y for x, y in zip(order, wei))
    if req < n * m:
        assert 9 * sum(order) <= n * m, "Sloppy solution?"
        ans += 1
    # print(n * m - req)
print(ans)
# a = []
# for line in lines:
#     a.append(tuple(map(int, line.split(","))))
# n = len(a)
