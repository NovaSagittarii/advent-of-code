import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

steps = lines[0]
adj = {}
for line in lines[2:]:
	a, bc = line.split(" = ")
	bc = bc[1:-1]
	b, c = bc.split(", ")
	adj[a] = (b, c)

curr = 'AAA'
i = 0
while curr != 'ZZZ':
	curr = adj[curr][0 if steps[i%len(steps)] == 'L' else 1]
	i += 1
print(i)