import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

"""
  3
  ^
2< > 0
  v
  1
"""
DIR = ((0,1), (1,0), (0,-1), (-1,0))
DIRX = {
    "R": 0,
    "D": 1,
    "L": 2,
    "U": 3,
}

pts = []
i, j = 0, 0
for line in lines:
    d, x, c = line.split()
    c = c[2:-1]
    x = int(c[:-1], 16)
    c = "RDLU"[int(c[-1])]
    di, dj = DIR[DIRX[c]]
    pts.append((i, j))
    i += di * x
    j += dj * x
pts.append((0, 0))
# print(pts)
# for pt in pts: print(f"vertex{pt};")

# https://11011110.github.io/blog/2021/04/17/picks-shoelaces.html
area = 0
boundary = 0
for i in range(len(pts)):
    x, y = pts[i]
    x2, y2 = pts[(i+1)%len(pts)]
    area += (x2-x)*(y2+y)
    boundary += (abs(x-x2) + abs(y-y2))
area //= 2
# https://en.wikipedia.org/wiki/Pick%27s_theorem
inside = int(area - boundary / 2 + 1)
print(inside, boundary)
ans = inside + boundary
print(ans)