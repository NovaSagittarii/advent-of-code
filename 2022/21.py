import math
import sys
lines = [l for l in sys.stdin]

def run(part2):
    vals = {}
    q = []
    for line in lines:
        l = line.split()
        a = l[0][:-1]
        if len(l) <= 2:
            vals[a] = int(l[-1])
        else:
            b, c = [l[i] for i in (1, 3)]
            if part2 and a == "root": ### part2
                l[2] = '='
            q.append((a, b, c, f"a{l[2]}b"))

    if part2: vals['humn'] = 'x' ### part2

    while len(q):
        qq,q = q,[]
        for n,a,b,expr in qq:
            # print(n, a, b, a in vals, b in vals, expr)
            if a in vals and b in vals:
                if type(vals[a]) == str or type(vals[b]) == str: # only ever runs if part 2 (string)
                    vals[n] = '(' + expr.replace('a', str(vals[a])).replace('b', str(vals[b])) + ')'
                else:
                    vals[n] = eval(expr.replace('a', str(vals[a])).replace('b', str(vals[b])))
            else:
                q.append((n,a,b,expr))
        # break
        # print(len(q))

    # print(vals)
    return vals['root']

print(run(False))
print(run(True))