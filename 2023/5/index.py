import sys
lines = [line.strip() for line in sys.stdin]

sections = '\n'.join(lines).split('\n\n')
seeds, *rest = sections

arrayint = lambda arr: list(int(x) for x in arr)

seeds = arrayint(seeds.split()[1:])
maps = list(list(arrayint(line.split()) for line in seg.split('\n')[1:]) for seg in rest)

final_locations = []
for seed in seeds:
    x = seed
    for mapping in maps:
        for dest, src, length in mapping:
            if src <= x < src + length:
                x = dest + (x - src)
                break
    final_locations.append(x)

print(min(final_locations))