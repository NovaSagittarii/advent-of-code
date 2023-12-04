import sys
lines = [line.strip() for line in sys.stdin]

for i, line in enumerate(lines):
	card, content = line.split(': ')
	win, num = [[int(x) for x in l.strip().split()] for l in content.split(' | ')]
	pts = 0
	for x in num:
		if x in win:
			pts += 1
	lines[i] = pts
dp = [1 for i in lines]
for i in range(len(dp)):
	for j in range(lines[i]):
		dp[i+j+1] += dp[i]
# print(dp)
print(sum(dp))