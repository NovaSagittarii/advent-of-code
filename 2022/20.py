import math
import sys
lines = [l for l in sys.stdin]

# order = list(map(int, filter(lambda x:x, lines)))

# print(order, ints)
# order.remove(0) # dont touch 0
# print(order, ints)
# m = len(order)

def indexOf(l, i, k):
	for j in range(len(l)):
		if l[j][k] == i:
			return j
# def debug(x,dx):
# 	i = indexOf(ints, 0, 1) # i = ints.index(0)
# 	print([x[1] for x in ints], x, x%n) # [*ints[i:], *ints[:i]]
# if n < 100: debug(0,0)

# print(len(set(x[0] for x in ints)))

# for x in order: # t in range(m):
	# if x == 0: continue
	# x = order[t%m]
def decrypt(multiplier, mixes):
	ints = list((a,b*multiplier) for a,b in enumerate(map(int, filter(lambda x:x, lines))))
	n = len(ints)
	for mixcount in range(mixes):
		for a in range(n):
			# i = ints.index(x)
			i = indexOf(ints, a, 0)
			x = ints[i][1]%(n-1) # ah.... its n-1 to cycle, not n
			temp = ints[i]
			# print(ints)
			for j in range(abs(x)%n):
				ints[(i+j)%n] = ints[(i+j+1)%n]
			ints[(i+x)%n] = temp
			# if n < 100: debug(ints[i][1],0)
			
	# if n < 100: debug(0,0)

	# print(len(set(x[0] for x in ints)))

	i = indexOf(ints, 0, 1) # i = ints.index(0)
	p1 = 0
	for j in (1000,2000,3000):
		d = ints[(i+j)%n][1]
		# print(d, end=' ')
		p1 += d
	# print()
	return p1

print(decrypt(1, 1))
print(decrypt(811589153, 10))