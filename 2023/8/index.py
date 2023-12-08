import math
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

curr = [curr for curr in adj.keys() if curr[-1] == 'A']

hist = [[] for i in curr]
his2 = [[] for i in curr]

i = 0
ok = False
while not ok:
    ok = True
    for j in range(len(curr)):
        curr[j] = adj[curr[j]][0 if steps[i%len(steps)] == 'L' else 1]
    i += 1
    for j, w in enumerate(curr):
        if w[-1] != 'Z':
            ok = False
            continue
        else:
            if len(hist[j]): his2[j].append(i - hist[j][-1][0])
            hist[j].append((i, w))
    if i > 100000:
        print(hist)
        cycles = [x[0] for x in his2]
        print(cycles)
        print(math.lcm(*cycles))
        
        break
print(i)
