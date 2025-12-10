import math
import re
import sys

lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

tot = 0
for line in lines:
    a, *choice, b = line.split()
    n = len(a) - 2
    a = sum(1 << i for i, x in enumerate(a[1:-1]) if x == "#")

    def parse(a):
        return sum(1 << int(x) for x in a[1:-1].split(","))

    choice = tuple(map(parse, choice))
    # print(a, bin(a), [bin(x) for x in choice], b)
    k = len(choice)
    best = 7893589235
    for mask in range(1 << k):
        cost = 0
        res = 0
        taken = []
        for b, bmask in enumerate(choice):
            if (1 << b) & mask:
                res ^= bmask
                cost += 1
                taken.append(bmask)
        # print(a, res, taken)
        if a == res:
            best = min(best, cost)
    # print(best)
    tot += best
print(tot)
