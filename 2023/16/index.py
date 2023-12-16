import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

lines = [list(line) for line in lines]

n = len(lines)
m = len(lines[0])
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
## \ >v , v>, 
#  3
#  ^
#2< > 0
#  v
#  1
def startfrom(INIT=(0, 0, 0)):
    q = [INIT]
    vis = [[[False,False,False,False] for w in line] for line in lines]
    mapping = {
        "|": ((1,3), (1,), (1,3), (3,)),
        "-": ((0,), (0,2), (2,), (0,2)),
        "/":  ((3,), (2,), (1,), (0,)),
        "\\": ((1,), (0,), (3,), (2,)),
        ".":  ((0,), (1,), (2,), (3,)),
    }
    while len(q):
        qq = []
        for i, j, d in q:
            if vis[i][j][d]: continue
            vis[i][j][d] = True
            for dd in mapping[lines[i][j]][d]:
                di, dj = DIRS[dd]
                ni = i+di
                nj = j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    qq.append((ni, nj, dd))
        q = qq

    # for line in vis:
    #     print("".join("#" if max(x) else "." for x in line))

    ans = 0
    for line in vis:
        for cell in line:
            ok = False
            for w in cell:
                if w:
                    ok = True
            if ok: ans += 1
    # print(ans)
    return ans

print(startfrom())
ans = 0
for i in range(n):
    ans = max(ans, startfrom((i, 0, 0)))
    ans = max(ans, startfrom((i, m-1, 2)))
for j in range(m):
    ans = max(ans, startfrom((0, j, 1)))
    ans = max(ans, startfrom((n-1, j, 3)))
print(ans)