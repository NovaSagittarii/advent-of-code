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

def search(start='AA', opened=0, time=30):
    # pos, totalrelease, release, nth bit is useful valve open
    q = [(start, 0, 0, opened)]
    visited = set()
    big = 0
    bigState = None
    for i in range(time):
        # print(i, len(q))
        p = q
        q = []
        for n in p:
            pos, total, rate, opened = n
            k = pos + str(total) + '-' + str(opened)
            if k in visited: continue
            visited.add(k)
            potential = total + rate*(time-i)
            if potential > big:
                big = potential
                bigState = n
                # print(bigState, end="")
            if opened == (1<<len(useful))-1: continue
            total += rate
            if pos in usefulDict.keys():
                valveBit = (1<<usefulDict[pos])
                if opened&valveBit == 0:
                    v = usefulDict[pos]
                    q.append((pos, total, rate + valves[pos][0], opened|valveBit))
            for v in valves[pos][1]:
                q.append((v, total, rate, opened))
    #print(big, bigState, bin(bigState[-1]))
    return big
trueBig = 0
last = (1<<len(useful))//2
v = set()
for i in range(last)[::-1]:
    print(i, last, end=" ")
    j = ((1<<len(useful))-1) ^ i
    # print(bin(i), bin(j))
    candidate = search('AA', i, 26) + search('AA', j, 26)
    trueBig = max(candidate, trueBig)
    print(trueBig)
print(trueBig)
