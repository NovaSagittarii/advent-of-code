import math
import re
import sys
import heapq
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

s = lines[0]

a = []
empty = []
exists = []
for i, c in enumerate(s):
    if i % 2 == 0:
        for j in range(int(c)):
            heapq.heappush(exists, -len(a))
            a.append(i//2)
    else:
        for j in range(int(c)):
            empty.append(len(a))
            a.append(0)

n = len(a)
i = n-1
empty = empty[::-1]

# print(empty)
# print(exists)
# print(*a)
while empty and exists:
    i = -heapq.heappop(exists)
    j = empty.pop()
    if i < j: continue
    # print(f"{i} => {j}")
    a[j] = a[i]
    a[i] = 0
    heapq.heappush(exists, -j)

# print(*a)
ans = 0
for i, x in enumerate(a):
    ans += i * x
print(ans)
