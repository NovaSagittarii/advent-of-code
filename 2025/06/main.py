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
    A.append(line.split())

ans = 0
n = len(A)
m = len(A[0])
for j in range(m):
    op = A[-1][j]
    tot = 0
    if op == '*': tot = 1
    for i in range(n-1):
        x = int(A[i][j])
        if op == '*': tot *= x
        else: tot += x
    ans += tot
print(ans)
