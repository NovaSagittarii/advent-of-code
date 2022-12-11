import sys
lines = [line.strip() for line in sys.stdin]

monkeys = []

for i in range(len(lines))[::7]:
    a, b, c, d, e, f = [lines[i+j] for j in range(6)]
    monkey = int(a.split()[1][:-1])
    items = list(map(int, b.replace(',', "").split()[2:]))
    expression = c.split('=')[1].strip()
    div = int(d.split()[-1])
    iftrue = int(e.split()[-1])
    iffalse = int(f.split()[-1])

# soo... my laptop died as i was submitting and since i use online compiler, the code is gone ... and i dont feel like rewriting it so have some pseudocode

# just do it normally 20 or 10000 times going through the monkeys normally
# use eval(expression.replace('old', worry)) to get new worry
# and for monkeyDiv in monkeys: x = lcm(x, monkeyDiv) to get the lcm