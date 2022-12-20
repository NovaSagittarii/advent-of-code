import math
import sys
lines = [l for l in sys.stdin]

def indexOf(l, i, k):
	for j in range(len(l)):
		if l[j][k] == i:
			return j

def decrypt(multiplier, mixes):
	ints = list((a,b*multiplier) for a,b in enumerate(map(int, filter(lambda x:x, lines))))
	n = len(ints)
	for mixcount in range(mixes):
		for a in range(n):
			i = indexOf(ints, a, 0)
			x = ints[i][1]%(n-1) # ah.... its n-1 to cycle, not n
			temp = ints[i]
			for j in range(abs(x)%n):
				ints[(i+j)%n] = ints[(i+j+1)%n]
			ints[(i+x)%n] = temp

	i = indexOf(ints, 0, 1)
	p1 = 0
	for j in (1000,2000,3000):
		d = ints[(i+j)%n][1]
		p1 += d
	return p1

print(decrypt(1, 1))
print(decrypt(811589153, 10))