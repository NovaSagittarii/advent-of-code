import sys
lines = [line.strip() for line in sys.stdin]

SIZE = 4000000 # 20
rows = [[] for i in range(SIZE+1)]

for line in lines:
    a = (line+":").split(' ')
    sx, sy, bx, by = map(lambda x: int(x[2:-1]), [a[2], a[3], a[8], a[9]])
    # print(sx, sy, bx, by)
    d = abs(sx-bx) + abs(sy-by)
    for y in range(max(0, sy-d), min(SIZE,sy+d+1)+1):
        l = sx - d + abs(sy-y)
        r = sx + d - abs(sy-y)
        if l > r: continue
        rows[y].append((l, r))
    if by == y:
        # rows[y].append((bx, bx))
        pass

for y, row in enumerate(rows):
    row.sort(key=lambda x:x[1])
    row.sort(key=lambda x:x[0])
    x = 0
    for l, r in row:
        if x < l:
            for x in range(x+1, l):
                print(x, y, 4000000*x+y)
        x = max(r, x)
    if x <= SIZE:
        print(x, y, 4000000*x+y)
print(len(rows))