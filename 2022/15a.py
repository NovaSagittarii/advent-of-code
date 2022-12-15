import sys
lines = [line.strip() for line in sys.stdin]

y = 2000000
x = set()
xb = set()
for line in lines:
	a = (line+":").split(' ')
	sx, sy, bx, by = map(lambda x: int(x[2:-1]), [a[2], a[3], a[8], a[9]])
	# print(sx, sy, bx, by)
	d = abs(sx-bx) + abs(sy-by)
	l = sx - d + abs(sy-y)
	r = sx + d - abs(sy-y)
	if by == y:
	    xb.add(bx)
	if l > r: continue
	for i in range(l, r+1):
	    if i not in x:
	        x.add(i)
for i in xb: x.remove(i)
# print(x)
print(len(x))

