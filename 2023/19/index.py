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