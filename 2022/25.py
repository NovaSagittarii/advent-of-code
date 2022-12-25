import math
import sys
lines = [l for l in sys.stdin]

chars = {
	"=": -2,
	"-": -1,
	"0": 0,
	"1": 1,
	"2": 2
}
charIndex = list("=-012")

def snafu(s):
	total = 0
	for i in range(len(s)):
		total += chars[s[i]] * (5**(len(s)-1-i))
	return total

p1 = 0
for line in lines:
	s = line.strip()
	
	# print(total)
	p1 += snafu(s)

print(p1)