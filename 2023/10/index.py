import math
import sys
lines = ['.'+line.strip()+'.' for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)


m = len(lines[0]) + 1
lines = ['.'*m, *lines, '.'*m]
n = len(lines) + 1

# for line in lines: print(line)

q = []
vis = [[0 for i in range(m)] for i in range(n)]
adj = [[[] for i in range(m)] for i in range(n)]

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        up = char in '|LJ'
        down = char in '|7F'
        left = char in 'J7-'
        right = char in 'LF-'
        if down:
            adj[i][j].append((i+1, j))
            adj[i+1][j].append((i, j))
        if up:
            adj[i][j].append((i-1, j))
            adj[i-1][j].append((i, j))
        if right:
            adj[i][j].append((i, j+1))
            adj[i][j+1].append((i, j))
        if left:
            adj[i][j].append((i, j-1))
            adj[i][j-1].append((i, j))
        if char == 'S':
            q.append((i, j))
            adj[i][j].append((i, j+1))
            adj[i][j].append((i, j-1))
            adj[i][j].append((i+1, j))
            adj[i][j].append((i-1, j))

# only allow agreement
for row in adj:
    for i, adjl in enumerate(row):
        adjlFiltered = []
        ok = {}
        for pair in adjl:
            if pair not in ok: ok[pair] = 0
            ok[pair] += 1
        for k, v in ok.items():
            if v >= 2:
                adjlFiltered.append(k)
        row[i] = adjlFiltered

rounds = 0
while q:
    nq = []
    for i, j in q:
        if vis[i][j]: continue
        vis[i][j] = rounds
        for ni, nj in adj[i][j]:
            if not vis[ni][nj]:
                nq.append((ni, nj))
    if len(nq): rounds += 1
    q = nq

# for lien in vis: print(lien)

print(rounds)