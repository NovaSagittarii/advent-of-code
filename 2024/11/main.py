import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

A = arrayint(lines[0].split())

def process(x):
    s = str(x)
    if x == 0:
        return (1, )
    elif len(s) % 2 == 0:
        w = 10 ** (len(s)//2)
        return (x // w, x % w)
    else:
        return (x*2024, )

cts = {}
for x in A:
    if x not in cts: cts[x] = 0
    cts[x] += 1
    # print(x, process(x))

for round in range(25):
    ncts = {}
    for k, v in cts.items():
        for x in process(k):
            if x not in ncts: ncts[x] = 0
            ncts[x] += v
    cts = ncts
    print(round, sum(cts.values()))
print(sum(cts.values()))