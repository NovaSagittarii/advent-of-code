grid = []
while 1:
    try:
        grid.append(list(map(int, list(input().strip()))))
    except Exception:
        break

visible = [[0 for i in row] for row in grid]

w = len(grid[0])
h = len(grid)

def scan(x, y, dx, dy):
    visible[y][x] = 1
    prev = grid[y][x]
    while x >= 0 and x < w and y >= 0 and y < h:
        x += dx
        y += dy
        try:
            if grid[y][x] > prev:
                visible[y][x] = 1
            prev = max(prev, grid[y][x])
        except:
            break
    
for i in range(h):
    scan(0, i, 1, 0)
    scan(w-1, i, -1, 0)
for j in range(w):
    scan(j, 0, 0, 1)
    scan(j, h-1, 0, -1)

#print(grid)
#print(visible)

print(sum(sum(row) for row in visible))


def scan2(y,x, dx, dy):
    val = 0
    prev = grid[y][x]
    # if x == 0 or x == w-1 or y == 0 or y == h-1: return 0
    while x+dx >= 0 and x+dx < w and y+dy >= 0 and y+dy < h:
        x += dx
        y += dy
        try:
            grid[y][x]
            if grid[y][x] < prev:
                val += 1
            elif grid[y][x] == prev:
                val += 1 
                break
            else:
                val += 1
                break
            # prev = max(prev, grid[y][x])
        except:
            break
    return val

print()

best = 0
for i in range(h):
    for j in range(w):
        candidate = scan2(i, j, 1, 0) * scan2(i, j, -1, 0) * scan2(i, j, 0, 1) * scan2(i, j, 0, -1)
        # if(candidate>0): print(scan2(i, j, 1, 0) , scan2(i, j, -1, 0) , scan2(i, j, 0, 1) , scan2(i, j, 0, -1))
        best = max(candidate, best)
        #print(candidate, end=' ')
    #print()
print(best)
# print(grid[3][2])
# print(scan2(3,2,1,0), scan2(3,2,-1,0), scan2(3,2,0,1), scan2(3,2,0,-1))

        