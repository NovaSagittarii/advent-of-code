import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

A = lines[0].split(', ')
Q = lines[2:]

ans = 0
for q in Q:
    n = len(q)
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(n):
        if not dp[i]: continue
        for a in A:
            if i+len(a) > n: continue
            ok = True
            for j, c in enumerate(a):
                if q[i+j] != c:
                    ok = False
                    break
            if ok:
                dp[i + len(a)] += dp[i]
    # print(q, dp[-1])
    ans += dp[-1]
print(ans)
