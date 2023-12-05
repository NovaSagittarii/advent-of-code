import sys
lines = [line.strip() for line in sys.stdin]

sections = '\n'.join(lines).split('\n\n')
seeds, *rest = sections

arrayint = lambda arr: list(int(x) for x in arr)

seeds = arrayint(seeds.split()[1:])
maps = list(list(arrayint(line.split()) for line in seg.split('\n')[1:]) for seg in rest)

for i, mapping in enumerate(maps):
    # print(mapping)
    mapping.sort(key=lambda x: x[1])
    BIG = int(1e10)
    mapping.append((BIG, BIG, BIG))
    needs = []
    prev = 0
    for _d, s, l in mapping:
        if s > prev:
            needs.append((prev, prev, s-prev))
        prev = s+l
    mapping += needs
    mapping.sort(key=lambda x: x[1])
    # print(mapping)

def intersects(A, B):
    al, ar = A
    bl, br = B
    return bl <= al < br or bl <= ar < br or al <= bl < ar or al <= br < ar
def intersection(A, B):
    al, ar = A
    bl, br = B
    return (max(al, bl), min(ar, br))
def intersection_length(A, B):
    l, r = intersection(A, B)
    return r-l

ans = 89234890234890234
for i in range(len(seeds))[::2]:
    ints = [(seeds[i], seeds[i]+seeds[i+1])]
    print('start', ints)
    for mapping in maps:
        newints = []
        for dest, src, length in mapping:
            S = (src, src+length)
            for intv in ints:
                inl = intersection_length(S, intv)
                if inl > 0:
                    o = intersection(S, intv)[0] - S[0]
                    newints.append((dest + o, dest + inl + o))
        ints = newints
        print(ints)
    ints.sort(key=lambda x: x[0])
    ans = min(ans, ints[0][0])
print(ans)