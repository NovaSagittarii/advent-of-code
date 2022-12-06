
total = 0
dist = {
    "COM": 0,
}
later = []
edges = {}
try:
    while True:
        x = input()
        a, b = x.split(')')
        later.append((a,b))
        if a not in edges: edges[a] = []
        if b not in edges: edges[b] = []
        edges[a].append(b)
        edges[b].append(a)
except Exception:
    pass

while len(later):
    todo = later
    later = []
    for a, b in todo:
        if a in dist:
            dist[b] = dist[a] + 1
            total += dist[b]
        else:
            later.append((a,b))

print(total)

d = -3
q = ["SAN"]
v = set()
while len(q):
    p = q
    q = []
    d += 1
    for n in p:
        if n in v: continue
        v.add(n)
        # print(n)
        if n == "YOU":
            print(d)
            d = None
            break
        for o in edges[n]:
            q.append(o)
    if d == None: break