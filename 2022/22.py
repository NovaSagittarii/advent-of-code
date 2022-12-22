import math
import sys
lines = [l for l in sys.stdin]
 
w = len(lines[0])

dirDisplay = ">v<^"
directions = [(1,0), (0,1), (-1,0), (0,-1)] # >v<^
grid = [list(line.replace('\n', '') + ' '*(w-len(line))) for line in lines[:-2]]
history = [[" " for i in range(len(lines[0]))] for i in grid]
path = lines[-1] + "X" # uhh i didnt do movement properly lol

z = min(len(l.strip()) for l in lines[:-2])
h = len(grid)
w = max(len(g) for g in grid)

print("z", z)
print("h", h)
print("w", w)

def outOfBounds(grid, nx, ny):
	return (ny < 0 or nx < 0 or ny >= len(grid) or nx >= len(grid[ny]))

def getCorners(sx, sy):
	o = []
	for i in range(0, 2):
		for j in range(0, 2):
			o.append( (sx+i*(z-1), sy+j*(z-1)) )
	return o

side = 0
netgrid = [[None for j in range(w//z+2)] for i in range(h//z+2)]
netcoords = []
netcoordsGrid = []
netcorners = []
for i in range(h//z):
	for j in range(w//z):
		if not outOfBounds(grid, j*z, i*z) and grid[i*z][j*z] != ' ':
			netgrid[i+1][j+1] = (side, -1)
			netcoords.append((j+1, i+1))
			netcoordsGrid.append((j*z, i*z))
			netcorners.append(getCorners(j*z, i*z))
			# print(getCorners(j*z, i*z))
			# for x,y in getCorners(j*z, i*z): grid[y][x] = 'X'
			side += 1
# print("\n".join("".join(str(x[0]) if x else ' ' for x in l) for l in netgrid))

def netEdge(netsurface, direction):
	corners = netcorners[netsurface]
	sxy = netcoordsGrid[netsurface]
	# print(corners, sxy)
	o = []
	for corner in corners:
		ok = True
		for k in range(2): # x and y dimensions
			xy = corner
			if directions[direction][k] != 0 and (xy[k] > sxy[k]) != (directions[direction][k] > 0):
				ok = False
		if ok: o.append(corner)
	return o
def manhattanDist(x, y):
	return sum(abs(x[k] - y[k]) for k in range(len(x)))
def addVector(a, b):
	return (a[k] + b[k] for k in range(len(a)))

warps = {}
for i in range(-1, len(grid)+1): warps[i] = {}

def linkEdges(a, b, prevCorners=None):
	# print("link", a, b)
	ae = netEdge(*a)
	be = netEdge(*b)
	ae.sort(key=lambda x:min(manhattanDist(x, y) for y in (prevCorners or be)))
	be.sort(key=lambda x:min(manhattanDist(x, y) for y in (prevCorners or ae)))
	print("link", a, b, ae, be, 'pc', prevCorners)

	adx, ady = (max(-1, min(1, ae[1][k] - ae[0][k])) for k in range(2))
	bdx, bdy = (max(-1, min(1, be[1][k] - be[0][k])) for k in range(2))
	ax, ay, bx, by = None,None,None,None
	for t in range(manhattanDist(ae[0], ae[1])+1):
		ax, ay, bx, by = ae[0][0]+adx*t, ae[0][1]+ady*t, be[0][0]+bdx*t, be[0][1]+bdy*t
		# print("warp", ax, ay, bx, by)
		# ax + direction[a[1] # showering rn
		a1x, a1y = addVector((ax, ay), directions[a[1]])
		b1x, b1y = addVector((bx, by), directions[b[1]])
		# if ax in warps[ay] or bx in warps[by]: print("collide??")
		warps[a1y][a1x*10+a[1]] = (bx, by, (b[1]+2)%4)
		warps[b1y][b1x*10+b[1]] = (ax, ay, (a[1]+2)%4)
		# if not outOfBounds(grid, a1x, a1x): grid[a1y][a1x] = grid[by][bx] = "ASDFGHJKL"[t]
		# if not outOfBounds(grid, b1x, b1x): grid[b1y][b1x] = grid[ay][ax] = "QWERTYUIO"[t]
	return ((ax, ay), (bx, by))

q = []
for x, y in netcoords:
	side = netgrid[y][x][0]
	for direction in range(len(directions)):
		dx, dy = directions[direction]
		nx, ny = x+dx, y+dy
		if netgrid[ny][nx] != None: # collide
			if netgrid[ny][nx][1] < 0: continue # ran into solid
			usedCorners = linkEdges(netgrid[ny][nx], (side, direction)) # print("link", netgrid[ny][nx], (side, direction))
			# print(netEdge(*netgrid[ny][nx]), netEdge(side, direction)) # print(netcorners[netgrid[ny][nx][0]])
			netgrid[ny][nx] = [(netgrid[ny][nx][0], side), -2]
			q.append(( ((nx,ny),) ,usedCorners))
		else: # place
			netgrid[ny][nx] = [side, direction]
# print("\n".join("".join(str(x[0])[0] if x and x[1]>=0 else ' ' for x in l) for l in netgrid))

while len(q):
	qq,q = q,[]
	# print("qq", qq[0])
	for n,uc in qq:
		touch = []
		# print("n", n)
		for x,y in n:
			for dx in range(-1,2):
				for dy in range(-1,2):
					nx, ny = x+dx, y+dy
					if not outOfBounds(netgrid,nx,ny) and netgrid[ny][nx] != None and netgrid[ny][nx][1] >= 0:
						touch.append((nx, ny))
						# touch.append(netgrid[ny][nx])
		# print("x",x,"y",y)
		# print(netgrid[y][x][0], touch)
		if len(touch) < 2: continue
		if set((netgrid[y][x][0],)) != set(netgrid[y][x][0] for x,y in touch): # there ever only 1 connection between two faces
			usedCorners = linkEdges(*[netgrid[y][x] for x,y in touch], uc) # print("link", *[netgrid[y][x] for x,y in touch])
			for x,y in touch:
				netgrid[y][x][1] = -2 # netgrid[y][x] = ((netgrid[y][x][0] for x,y in touch), -2)
				q.append((touch, usedCorners))

# print(warps)
# print("\n".join(["".join(x) for x in grid]))

def solve(partTwo=False):
	grid2 = [[g for g in l] for l in grid]

	x = grid[0].index('.')
	y = 0
	direction = 0

	j = 0
	for i in range(len(path)):
		if path[i] == 'L' or path[i] == 'R' or path[i] == 'X':
			instruction = path[j:i+1]
			j = i+1

			steps = int(instruction[:-1])
			# print(steps, instruction[-1])

			for t in range(steps):
				grid2[y][x] = dirDisplay[direction]

				dx,dy = directions[direction]
				nx = x + dx
				ny = y + dy
				p = ' ' if outOfBounds(grid, nx, ny) else grid[ny][nx]
				if p == '.' or (p!='#' and p!=' '):
					x, y = nx, ny
				elif p == '#':
					break
				elif p == ' ':
					# print(nx-dx,ny-dy)
					ndirection = direction
					if not partTwo: # wrapping behavior
						while not outOfBounds(grid, nx-dx, ny-dy) and grid[ny-dy][nx-dx] != ' ': # go backwards until you run into empty
							nx -= dx
							ny -= dy
							# print(nx-dx,ny-dy)
					else: # wacky cube action
						print("go into warp", nx, ny, warps[ny][nx*10+direction])
						# nx,ny,ndirection = warps[ny-dy][nx-dx]
						nx,ny,ndirection = warps[ny][nx*10+direction]
					if grid[ny][nx] == '#': break # ran into wall
					elif grid[ny][nx] == '.':
						x, y, direction = nx, ny, ndirection

			if instruction[-1] != 'X':
				direction = (direction + (1 if instruction[-1] == 'R' else -1)) % len(directions)
		grid2[y][x] = dirDisplay[direction]
	print("\n".join(["".join(x) for x in grid2]))
	# print(x, y, direction)

	row = y+1
	col = x+1
	print(row, col, direction)
	print(row*1000 + col*4 + direction)

# solve()
solve(True)