import math
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

emptyrow = [True for _ in lines]
emptycol = [True for _ in lines[0]]
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != '.':
            emptyrow[i] = False
            emptycol[j] = False

newlines = []
for i, line in enumerate(lines):
    newline = ""
    for j, c in enumerate(line):
        newline += c
        if emptycol[j]: newline += '.'
    newlines.append(newline)
    if emptyrow[i]: newlines.append('.' * len(newlines[0]))

print("\n".join(newlines))
lines = newlines

coords = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != '.':
            coords.append((i, j))

ans = 0
for i, c in enumerate(coords):
    x1, y1 = c
    for d in coords[i+1:]:
        x2, y2 = d
        ans += abs(x1-x2) + abs(y1-y2)
print(ans)