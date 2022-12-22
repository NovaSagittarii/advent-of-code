import math
import sys
lines = [l for l in sys.stdin]
 
w = len(lines[0])

dirDisplay = ">v<^"
directions = [(1,0), (0,1), (-1,0), (0,-1)] # >v<^
grid = [list(line.replace('\n', '') + ' '*(w-len(line))) for line in lines[:-2]]
history = [[" " for i in range(len(lines[0]))] for i in grid]
path = lines[-1]

z = min(len(l.strip()) for l in lines[:-2])
h = len(grid)
w = max(len(g) for g in grid)

print("z", z)
print("h", h)
print("w", w)

def outOfBounds(grid, nx, ny):
	return (ny < 0 or nx < 0 or ny >= len(grid) or nx >= len(grid[ny]))

x = grid[0].index('.')
y = 0
direction = 0


j = 0
for i in range(len(path)):
	if path[i] == 'L' or path[i] == 'R':
		instruction = path[j:i+1]
		j = i+1

		steps = int(instruction[:-1])

		dx,dy = directions[direction]
		for t in range(steps):
			nx = x + dx
			ny = y + dy
			p = ' ' if outOfBounds(grid, nx, ny) else grid[ny][nx]
			if p == '.' or (p!='#' and p!=' '):
				x, y = nx, ny
			elif p == '#':
				break
			elif p == ' ':
				# print(nx-dx,ny-dy)
				while not outOfBounds(grid, nx-dx, ny-dy) and grid[ny-dy][nx-dx] != ' ': # go backwards until you run into empty
					nx -= dx
					ny -= dy
					# print(nx-dx,ny-dy)
				if grid[ny][nx] == '#': break # ran into wall
				elif grid[ny][nx] == '.':
					x, y = nx, ny
			# grid[y][x] = dirDisplay[direction]

		direction = (direction + (1 if instruction[-1] == 'R' else -1)) % len(directions)

# print("\n".join(["".join(x) for x in grid]))
print(x, y, direction)

row = y+1
col = x+1
print(row*1000 + col*4 + direction)