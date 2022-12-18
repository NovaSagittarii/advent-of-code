import sys
lines = [l for l in sys.stdin]

#print (lines)

n = 27
g =[[[0 for i in range(n)] for i in range(n)] for i in range(n)]
p = []

for l in lines:
    x,y,z = map(int,l.split(','))
    g[x][y][z] = 1
    p.append((x,y,z))

q=[(0,0,0)]
while len(q):
    qq,q=q,[]
    for x,y,z in qq:
        if x<0 or x>=n or y<0 or y>= n or z<0 or z>=n:
            continue
        if g[x][y][z] != 0: continue
        g[x][y][z] = 2
        q.append((x+1,y,z))
        q.append((x-1,y,z))
        q.append((x,y+1,z))
        q.append((x,y-1,z))
        q.append((x,y,z+1))
        q.append((x,y,z-1))

ct = 0
ct2 = 0
for x,y,z in p:
    for dx in (-1,1):
        if g[x+dx][y][z] != 1: ct += 1
        if g[x][y+dx][z] != 1: ct += 1
        if g[x][y][z+dx] != 1: ct += 1
        
        if g[x+dx][y][z] > 1: ct2 += 1
        if g[x][y+dx][z] >1: ct2 += 1
        if g[x][y][z+dx]>1: ct2 += 1
print(ct, ct2)

