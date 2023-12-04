import sys
lines = [line.strip() for line in sys.stdin]

ans = 0
for line in lines:
	card, content = line.split(': ')
	win, num = [[int(x) for x in l.strip().split()] for l in content.split(' | ')]
	pts = 0
	for x in num:
		if x in win:
			if pts == 0: pts = 1
			else: pts *= 2
	ans += pts
print(ans)
