import sys
lines = [line.strip() for line in sys.stdin]

# v = 0
cycletime = [1]
for line in lines:
    op, x = (line+" 0").split()[:2]
    x = int(x)
    
    if op == "noop":
        cycletime.append(cycletime[-1])
    elif op == "addx":
        cycletime.append(cycletime[-1])
        cycletime.append(cycletime[-1] + x)

print(sum(map(lambda x: x*cycletime[x-1], [20, 60, 100, 140, 180, 220])))

for j in range(len(cycletime))[::40]:
    row = [" " for i in range(40)]
    for i in range(40):
        if abs(cycletime[i+j]-i) <= 1:
            row[i] = '#'
    print("".join(row))