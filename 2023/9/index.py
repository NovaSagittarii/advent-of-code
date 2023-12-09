import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

ans = 0
for line in lines:
	line = arrayint(line.split())[::-1]
	ls = [line]
	def nextline(l):
		out = []
		for i in range(len(l)-1):
			out.append(l[i+1] - l[i])
		return out
	def allzero(l):
		return max(l) == min(l) and l[0] == 0
	while not allzero(ls[-1]):
		ls.append(nextline(ls[-1]))
	for i, l in list(enumerate(ls))[::-1]:
		ls[i-1].append(ls[i-1][-1] + ls[i][-1])
	# print(ls)
	w = ls[0][-1]
	# print(w)
	ans += w
print(ans)