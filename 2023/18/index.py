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
# pts.append((0, 0))
for line in lines:
    d, x, c = line.split()
    c = c[2:-1]
    x = int(c[:-1], 16)
    c = "RDLU"[int(c[-1])]
    di, dj = DIR[DIRX[c]]
    pts.append((i, j))
    i += di * x
    j += dj * x
print(pts)
for pt in pts: print(f"vertex{pt};")

# https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
def onCorner(x1, y1, x2, y2, x3, y3, x, y):
    return x in (x1, x2, x3) and y in (y1, y2, y3)
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area (x1, y1, x2, y2, x3, y3)
    A1 = area (x, y, x2, y2, x3, y3)
    A2 = area (x1, y1, x, y, x3, y3)
    A3 = area (x1, y1, x2, y2, x, y)
    return A == A1 + A2 + A3

# https://stackoverflow.com/a/57503229
def angle3(x1, y1, x2, y2, x3, y3):
    lineA = ((x1, y1), (x2, y2))
    lineB = ((x2, y2), (x3, y3))
    line1Y1 = lineA[0][1]
    line1X1 = lineA[0][0]
    line1Y2 = lineA[1][1]
    line1X2 = lineA[1][0]

    line2Y1 = lineB[0][1]
    line2X1 = lineB[0][0]
    line2Y2 = lineB[1][1]
    line2X2 = lineB[1][0]

    #calculate angle between pairs of lines
    angle1 = math.atan2(line1Y1-line1Y2,line1X1-line1X2)
    angle2 = math.atan2(line2Y1-line2Y2,line2X1-line2X2)
    angleDegrees = (angle1-angle2) * 360 / (2*math.pi)
    return (angleDegrees + 360) % 360

# https://www.geometrictools.com/Documentation/TriangulationByEarClipping.pdf
ans = 0
while len(pts) >= 3:
    change = False
    for i in range(len(pts)):
        n = len(pts)
        if i >= len(pts): break
        ok = True
        triangle = (*pts[(i-1)%n], *pts[i%n], *pts[(i+1)%n])
        if angle3(*triangle) >= 179 and n > 3: continue
        # print((i-1)%len(pts), i, (i+1)%len(pts))
        for pt in pts:
            if onCorner(*triangle, *pt): continue
            if isInside(*triangle, *pt):
                ok = False
        if ok or n == 3:
            ans += area(*triangle)
            # print(area(*triangle))
            # print(triangle, pts[i], area(*triangle))
            pts.remove(pts[i])
            print(f"triangle{triangle};")
            change = True 
            break
            # print(angle3(*triangle))
    # if not change: break
ans //= 2
print(ans)