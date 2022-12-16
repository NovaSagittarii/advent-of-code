import sys
lines = [line.strip() for line in sys.stdin]

import itertools

valves = {}

for line in lines:
    l = (line+",").split(' ')
    valve, rate, connected = l[1], int(l[4].split('=')[1][:-1]), [x[:-1] for x in l[9:]]
    valves[valve] = (rate, connected)
# print(valves)

valvesDict = {}
for i, v in enumerate(valves.keys()):
    valvesDict[v] = i

useful = list(filter(lambda k:valves[k][0] > 0, valves.keys()))
usefulDict = {}
for i, v in enumerate(useful):
    usefulDict[v] = i
# print([f'{x}={valves[x][0]}' for x in useful])

n = len(valves.keys())
apsp = [[999 for i in range(n)] for i in range(n)]
for v in valves.keys():
    a = valvesDict[v]
    apsp[a][a] = 0
    for u in valves[v][1]:
        b = valvesDict[u]
        apsp[a][b] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            apsp[i][j] = min(apsp[i][j], apsp[i][k] + apsp[k][j])
# print(apsp)

def search(start='AA', opened=0, time=30):
    # timeLeft, pos, totalrelease, release, nth bit is useful valve open
    q = [(time, start, 0, 0, opened)]
    visited = set()
    big = 0
    bigState = None
    while(len(q)):
        # print(len(q)) # i need progress
        p = q
        q = []
        for n in p:
            timeLeft, pos, total, rate, opened = n
            if timeLeft <= 0: continue
            k = pos + str(total) + '-' + str(opened)
            if k in visited: continue
            visited.add(k)
            potential = total + rate*timeLeft
            if potential > big:
                big = potential
                bigState = n
                # print(potential, bigState)
            # if opened == (1<<len(useful))-1: continue
            # total += rate
            for k in useful:
                valveBit = (1<<usefulDict[k])
                if opened&valveBit == 0:
                    if pos == k:
                        q.append((timeLeft-1, pos, total + rate, rate + valves[pos][0], opened|valveBit))
                    else:
                        a = valvesDict[pos]
                        b = valvesDict[k]
                        q.append((timeLeft-apsp[a][b], k, total + rate*apsp[a][b], rate, opened))
    # print(big, bigState, bin(bigState[-1]))
    return big

trueBig = 0
last = (1<<len(useful))//2
for i in range(last)[::-1]:
    print(i, last, end=" ")
    j = ((1<<len(useful))-1) ^ i
    # print(bin(i), bin(j))
    candidate = search('AA', i, 26) + search('AA', j, 26)
    trueBig = max(candidate, trueBig)
    print(trueBig)
print('p1', search('AA', 0, 30))
print('p2', trueBig)
