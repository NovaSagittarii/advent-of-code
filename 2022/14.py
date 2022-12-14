import sys
lines = [line.strip() for line in sys.stdin]

WIDTH = 1000
HEIGHT = 800
grid = [[' ' for i in range(WIDTH)] for i in range(HEIGHT)]

low = 0
for line in lines:
	coords = [tuple(map(int, coord.split(','))) for coord in line.split(' -> ')]
	for i in range(len(coords) - 1):
	    x1, y1 = coords[i]
	    x2, y2 = coords[i+1]
	    dx = min(1, max(-1, x2-x1))
	    dy = min(1, max(-1, y2-y1))
	    while x1 != x2 or y1 != y2:
	        grid[y1][x1] = '#'
	        x1 += dx
	        y1 += dy
	    grid[y1][x1] = '#'
	    low = max(y1+2, low)

def fillWithSand(grid):
    sands = 0
    sx = 500
    sy = 0
    while sy < HEIGHT-5:
        if grid[sy+1][sx] == ' ':
            sy += 1
        elif grid[sy+1][sx-1] == ' ':
            sy += 1
            sx -= 1
        elif grid[sy+1][sx+1] == ' ':
            sy += 1
            sx += 1
        else:
            grid[sy][sx] = 'o'
            sands += 1
            sx = 500
            sy = 0
            if grid[sy][sx] != ' ': break
    for w in grid[0:10]:
        print("".join(w[494:504]))
    return sands

print(fillWithSand(grid))

# clear sands
for row in grid:
    for i in range(len(row)):
        row[i] = ' ' if row[i] == 'o' else row[i]
for i in range(WIDTH): grid[low][i] = '#'
print(fillWithSand(grid))