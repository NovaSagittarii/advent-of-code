import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

pts = []

for line in lines:
    p, v = [arrayint(x.split(', ')) for x in line.split(' @ ')]
    pts.append((*p, *v))

from z3 import Int, Solver

t1 = Int('t1')
t2 = Int('t2')
t3 = Int('t3')
rx = Int('rx')
ry = Int('ry')
rz = Int('rz')
ex = Int('ex')
ey = Int('ey')
ez = Int('ez')
s = Solver()

s.add(pts[0][0] + pts[0][3] * t1 == rx + ex * t1)
s.add(pts[0][1] + pts[0][4] * t1 == ry + ey * t1)
s.add(pts[0][2] + pts[0][5] * t1 == rz + ez * t1)

s.add(pts[1][0] + pts[1][3] * t2 == rx + ex * t2)
s.add(pts[1][1] + pts[1][4] * t2 == ry + ey * t2)
s.add(pts[1][2] + pts[1][5] * t2 == rz + ez * t2)

s.add(pts[2][0] + pts[2][3] * t3 == rx + ex * t3)
s.add(pts[2][1] + pts[2][4] * t3 == ry + ey * t3)
s.add(pts[2][2] + pts[2][5] * t3 == rz + ez * t3)

print(s.check())

m = s.model()

r = (m[rx], m[ry], m[rz])
print(r)
print(sum(x.as_long() for x in r))