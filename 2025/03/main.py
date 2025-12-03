import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

ans = 0
ans2 = 0
for line in lines:
    n = len(line)
    def calc(k):
        cur = -1
        res = []
        for i in reversed(range(k)):
            for j in range(cur, n-i):
                if cur < 0 or line[j] > line[cur]:
                    cur = j
            res.append(line[cur])
            cur += 1
        # print(int("".join(res)))
        return int("".join(res))
    ans += calc(2)
    ans2 += calc(12)
print(ans)
print(ans2)
# assert ans == 357
# assert ans2 == 3121910778619
