import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

a = []
for line in lines:
    a.append(list(line))
n = len(a)
m = len(a[0])

dp = [[1 if c == 'S' else 0 for c in row] for row in a]
splits = 0
for i in range(0, n-1):
    for j in range(m):
        if a[i][j] == '^':
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j+1] += dp[i][j]
            splits += min(1, dp[i][j])
        else:
            dp[i+1][j] += dp[i][j]
    # print(splits)
print(splits)
print(sum(dp[-1]))
