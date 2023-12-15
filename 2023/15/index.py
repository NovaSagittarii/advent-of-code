import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

ans = 0
lines = lines[0].split(',')
hashmap = [[] for i in range(256)]
for line in lines:
    x = 0
    label = ""
    op = "?"
    focal = -1
    for c in line:
        if c in '=-':
            op = c
            break
        label += c
        x += ord(c)
        x *= 17
        x %= 256
    if op == '=': focal = int(line[-1])
    found = False
    if op == '=': # its linear search oclock
        for i, el in enumerate(hashmap[x]):
            l, v = el
            if l == label:
                found = True
                hashmap[x][i][1] = focal
        if not found:
            hashmap[x].append([label, focal])
    else:
        for i, el in enumerate(hashmap[x]):
            l, v = el
            if l == label:
                hashmap[x].remove(el)
#     print(label, op, focal, x)
# print (hashmap)
for i, lens in enumerate(hashmap):
    for j, el in enumerate(lens):
        # print(e)
        ans += (i+1) * (j+1) * el[1]
print(ans)
