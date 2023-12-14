import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

n = len(lines)
lines = [list(line) for line in lines]
for t in range(n):
    for i, line in enumerate(lines):
        if i == 0: continue
        for j in range(len(line)):
            if lines[i-1][j] == '.' and lines[i][j] == 'O':
                lines[i-1][j] = 'O'
                lines[i][j] = '.'

ans = 0
for i, line in enumerate(lines):
    for c in line:
        if c == 'O':
            ans += (n-i)
print(ans)