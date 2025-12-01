import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

x = 50
ans = 0
ans2 = 0
for line in lines:
    dx = (1 if line[0] == 'R' else -1) * int(line[1:])
    # x += dx
    for i in range(abs(dx)):
        x += 1 if dx > 0 else -1
        x %= 100
        assert x >= 0
        if x == 0: ans2 += 1
    if x == 0:
        ans += 1
print(ans)
print(ans2) # 6400 - 6504
