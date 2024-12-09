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
            a.append(-1)

ap = a[::]
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
    a[i] = -1
    heapq.heappush(exists, -j)

# print(*a)
ans = 0
for i, x in enumerate(a):
    ans += i * max(0, x)
print(ans)

a = ap
pos = [[0, 0]] # <start offset, sz>
for i, c in enumerate(s):
    c = int(c)
    if i % 2 == 0:
        pos[-1][1] = c # update size
        pos.append([pos[-1][0] + c, 0])
    else:
        pos[-1][0] += c # update offset

for w, sz in reversed(pos):
    # print(*a)
    l = -1
    for i in range(w):
        if a[i] == -1:
            if l == -1:
                l = i
            if i-l+1 == sz: # do the move
                for j in range(sz):
                    a[l+j] = a[w+j]
                    a[w+j] = -1
        else:
            l = -1

# print(*a)
ans = 0
for i, x in enumerate(a):
    ans += i * max(0, x)
print(ans)