import sys
lines = [line.strip() for line in sys.stdin]

# only 12 red cubes, 13 green cubes, and 14 blue cubes

ans = 0
for line in lines:
    words = line.split()
    id = int(words[1][:-1])
    prod = 1
    limit = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for set in line.split(': ')[1].split('; '):
        for xy in set.split(', '):
            x, col = xy.split()
            limit[col] = max(limit[col], int(x))
    for v in limit.values():
        prod *= v
    ans += prod

print(ans)