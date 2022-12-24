import math
import sys
lines = [l for l in sys.stdin]

directions = [(1,0), (0,1), (-1,0), (0,-1)] # >v<^
directionText = ">v<^"
directionsPlayer = [*directions, (0,0)]

grid = [[' ' if c == '.' else c for c in line.strip()] for line in lines]
w = len(grid[0])
h = len(grid)
cyclones = []

for i in range(h):
	for j in range(w):
		if grid[i][j] != ' ' and grid[i][j] != '#':
			cyclones.append((j,i,directionText.index(grid[i][j])))

states = []
visitedStates = set()
repeated = False
i = 0
while not repeated:
	grid2 = [[c if c == ' ' or c == '#' else ' ' for c in row] for row in grid]
	for cyclone in cyclones:
		x,y,d = cyclone
		dx,dy = directions[d]
		x = (x+dx*i-1)%(w-2)+1
		y = (y+dy*i-1)%(h-2)+1
		if grid2[y][x] != ' ':
			if type(grid2[y][x]) != int: grid2[y][x] = 1
			grid2[y][x] += 1
		else:
			grid2[y][x] = directionText[d]
	k = "\n".join("".join(str(c) for c in row) for row in grid2)
	if k in visitedStates:
		repeated = True
	else:
		states.append(grid2)
		visitedStates.add(k)
	i += 1

# for i, state in enumerate(states): print("\n".join("".join(str(c) for c in row) for row in state), i)

def traverse(x,y,t,paths):
	visited = set()
	q = [(x,y,t,0)]
	while len(q):
		qq,q = q,[]
		# print(qq[0][2], len(qq))
		for x,y,t,p in qq:
			# print(x,y,t)
			np = p
			if y == (h-1 if np % 2 == 0 else 0):
				np += 1
				# print(np, t, (x,y))
				if np >= paths:
					return t
			k = y*w+x+100000*(t%len(states))+10000*p
			if k in visited: continue
			visited.add(k)
			for dx,dy in directionsPlayer:
				nx,ny,nt = x+dx,y+dy,t+1
				if nx < 0 or nx >= w or ny < 0 or ny >= h: continue
				if states[nt%len(states)][ny][nx] != ' ': continue
				q.append((nx,ny,nt,np))
p1 = traverse(grid[0].index(' '), 0, 0, 1)
print("p1", p1)

p2 = traverse(grid[0].index(' '), 0, 0, 3)
print("p2", p2)