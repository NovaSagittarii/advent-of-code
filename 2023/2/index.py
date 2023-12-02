import sys
lines = [line.strip() for line in sys.stdin]

# only 12 red cubes, 13 green cubes, and 14 blue cubes

ans = 0
for line in lines:
    words = line.split()
    id = int(words[1][:-1])
    ok = True
    for set in line.split(': ')[1].split('; '):
        limit = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }
        for xy in set.split(', '):
            x, col = xy.split()
            limit[col] -= int(x)
        for v in limit.values():
            if v < 0:
                ok = False
    if ok: ans += id

print(ans)