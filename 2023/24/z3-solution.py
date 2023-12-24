import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

pts = []

for line in lines:
    p, v = [arrayint(x.split(', ')) for x in line.split(' @ ')]
    pts.append((*p, *v))

from z3 import BitVec, Solver

t1 = BitVec('t1', 64)
t2 = BitVec('t2', 64)
t3 = BitVec('t3', 64)
rx = BitVec('rx', 64)
ry = BitVec('ry', 64)
rz = BitVec('rz', 64)
ex = BitVec('ex', 64)
ey = BitVec('ey', 64)
ez = BitVec('ez', 64)
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