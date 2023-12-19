import math
import sys
import re
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

rlines, qlines = [block.split("\n") for block in ("\n".join(lines).split('\n\n'))]

routing = {}
for rline in rlines:
    label, conditions = rline[:-1].split('{')
    conditions = tuple(condition.split(':') for condition in conditions.split(','))
    routing[label] = conditions

mapping = tuple("xmas")
ans = 0
for qline in qlines:
    vals = [int(q.split('=')[1]) for q in qline[1:-1].split(',')]
    loc = "in"
    while loc != 'A' and loc != 'R':
        conditions = routing[loc]
        nloc = conditions[-1][0]
        for condition in conditions[:-1]:
            payload = condition[0]
            for i, c in enumerate(mapping):
                payload = re.sub(c, str(vals[i]), payload)
            if eval(payload):
                nloc = condition[1]
                break
        loc = nloc
    if loc == 'A': ans += sum(vals)
print(ans)

def split_ranges(ranges, idx, split):
    lrange = [list(r[::]) for r in ranges[::]]
    mrange = [list(r[::]) for r in ranges[::]]
    rrange = [list(r[::]) for r in ranges[::]]
    if ranges[idx][0] <= split < ranges[idx][1]:
        lrange[idx][1] = min(lrange[idx][1], split)
        mrange[idx][0] = split
        mrange[idx][1] = split+1
        rrange[idx][0] = max(lrange[idx][0], split+1)
    else:
        lrange = mrange = rrange = None
    # print(ranges, idx, split)
    # print(lrange, mrange, rrange)
    return (lrange, mrange, rrange)

def union_ranges(r1, r2):
    if r1 == None: return r2
    if r2 == None: return r1
    for i in range(4):
        r1[i][0] = min(r1[i][0], r2[i][0])
        r1[i][1] = max(r1[i][1], r2[i][1])
    return r1

# [10, 20)
# split 5  -> [10, 20)
# split 15 -> [10,15) [15,15) [16,20)

ans = 0
all_ranges = tuple((1, 4001) for _ in range(4))
q = [("in", all_ranges)]
while len(q):
    nq = []
    for loc, ranges in q:
        # print(loc, ranges)
        leftover = ranges
        if loc == 'R': continue
        if loc == 'A':
            possible = 1
            for r in ranges:
                possible *= r[1] - r[0]
            ans += possible
            continue
        for condition, goto in routing[loc][:-1]:
            if leftover == None: break
            i = mapping.index(condition[0])
            op = condition[1]
            threshold = int(condition[2:])
            L, M, R = split_ranges(leftover, i, threshold)
            if op == '>':
                leftover = union_ranges(L, M)
                nq.append((goto, R))
            elif op == '<':
                leftover = union_ranges(R, M)
                nq.append((goto, L))
            else: raise ValueError(f"operation not implemented {op}")
        nq.append((routing[loc][-1][0], leftover))
    q = tuple(x for x in nq if x[1] != None)
print(ans)