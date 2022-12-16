import sys
lines = [line.strip() for line in sys.stdin]

import itertools

valves = {}

for line in lines:
    l = (line+",").split(' ')
    valve, rate, connected = l[1], int(l[4].split('=')[1][:-1]), [x[:-1] for x in l[9:]]
    valves[valve] = (rate, connected)
print(valves)

useful = list(filter(lambda k:valves[k][0] > 0, valves.keys()))
usefulDict = {}
for i, v in enumerate(useful):
    usefulDict[v] = i
print([f'{x}={valves[x][0]}' for x in useful])

# pos, totalrelease, release, nth bit is useful valve open
q = [('AA', 0, 0, 0)]
visited = set()
big = 0
bigState = None
for i in range(30):
    print(i, len(q))
    p = q
    q = []
    for n in p:
        pos, total, rate, opened = n
        k = pos + str(total) + '-' + str(opened)
        if k in visited: continue
        visited.add(k)
        potential = total + rate*(30-i)
        if potential > big:
            big = potential
            bigState = n
            # print(bigState, end="")
        total += rate
        if pos in usefulDict.keys():
            valveBit = (1<<usefulDict[pos])
            if opened&valveBit == 0:
                v = usefulDict[pos]
                q.append((pos, total, rate + valves[pos][0], opened|valveBit))
        for v in valves[pos][1]:
            q.append((v, total, rate, opened))
print(big, bigState, bin(bigState[-1]))