import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))
DIRD = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1,-1), (-1,1), (1,-1), (1,1))

A = []
for line in lines:
    A.append(line)

n = len(A)
m = len(A[0])

tot = 0
tot2 = 0
for i in range(n):
    for j in range(m):
        for di, dj in DIRD:
            ok = True
            for k, c in enumerate("XMAS"):
                ni = i + di*k
                nj = j + dj*k
                if 0 <= ni < n and 0 <= nj < m:
                    if A[ni][nj] != c: ok = False
                else: ok = False
            if ok: tot += 1
        if A[i][j] == 'A' and i >= 1 and i < n-1 and j >= 1 and j < m-1:
            w = ""
            for di, dj in ((-1,-1),(-1,1),(1,1),(1,-1)):
                w += A[i+di][j+dj]
            if w in ("MMSS", "MSSM", "SSMM", "SMMS"):
                tot2 += 1
print(tot)
print(tot2)