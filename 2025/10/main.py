import sys
import numpy as np
import scipy.optimize

lines = [line.strip() for line in sys.stdin]

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

tot = 0
tot2 = 0
for line in lines:
    a, *choice, b = line.split()
    n = len(a) - 2
    a = sum(1 << i for i, x in enumerate(a[1:-1]) if x == "#")
    req = tuple(map(int, b[1:-1].split(',')))

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

    c = np.ones((k))
    b_eq = np.zeros((n))
    A_eq = np.zeros((n, k))
    for i, x in enumerate(choice):
        for j in range(n):
            if x & (1 << j):
                A_eq[j][i] = 1
    for i, x in enumerate(req):
        b_eq[i] = x
    res = scipy.optimize.linprog(c, A_eq=A_eq, b_eq=b_eq, integrality=1)
    assert res.success
    tot2 += round(res.fun)
    # print(res)

print(tot)
print(tot2)
assert tot2 != 15249, "WA"
