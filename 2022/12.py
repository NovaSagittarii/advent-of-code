import sys
lines = [line.strip() for line in sys.stdin]

grid = [[ord(c) - ord('a') for c in line] for line in lines]

starts = []
s, t = None, None

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == -14: # S
            grid[i][j] = 0
            s = (i, j)
        elif grid[i][j] == -28: # E
            grid[i][j] = ord('z') - ord('a')
            t = (i, j)
        if grid[i][j] == 0: # a or S
            starts.append((i, j))
print(grid)
print(s, t)

def search(first):
    steps = -1
    v = set()
    q = [first]
    while len(q):
        steps += 1
        p = q
        q = []
        for i,j in p:
            # print(i, j)
            here = grid[i][j]
            k = i+1e4*j
            if k in v: continue
            v.add(k)
            if i == t[0] and j == t[1]:
                # print(steps)
                # q.clear()
                return steps
            for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
                a, b = i+dy, j+dx
                if a >= 0 and b >= 0 and a < len(grid) and b < len(grid[0]):
                    there = grid[a][b]
                    #if there == -1: continue # visited
                    if here >= there-1:
                        q.append((a, b))
            #grid[i][j] = -1
    return 9999
print(search(s))
print(min(search(s) for s in starts))