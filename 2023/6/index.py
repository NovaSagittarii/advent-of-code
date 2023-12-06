import sys
lines = [line.strip() for line in sys.stdin]

arrayint = lambda arr: list(int(x) for x in arr)

time, dist = lines
times = tuple(arrayint(time.split()[1:]))
dists = tuple(arrayint(dist.split()[1:]))

print(times, dists)
ans = 1
for i in range(len(times)):
	t = times[i]
	d = dists[i]
	ways = 0
	for ct in range(0, t+1):
		dd = (t-ct)*ct
		if dd > d:
			ways += 1
	ans *= ways
print(ans)