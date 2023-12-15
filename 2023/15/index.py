import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

ans = 0
lines = lines[0].split(',')
for line in lines:
    x = 0
    op = "?"
    focal = -1
    for c in line:
        x += ord(c)
        x *= 17
        x %= 256
    ans += x
print(ans)
