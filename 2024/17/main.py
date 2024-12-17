import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

A = []
for line in lines:
    A.append(line)

reg = [0, 1, 2, 3, 0, 0, 0]
for i in range(3):
    reg[4+i] = int(A[i].split()[-1])
code = list(map(int, A[-1].split()[-1].split(',')))

print(reg, code)
pc = 0
out = []
while pc+1 < len(code):
    op1 = code[pc]
    op2 = code[pc+1]
    A = 4
    B = 5
    C = 6
    if op1 == 0: # adv
        reg[A] = reg[A] // 2 ** reg[op2]
    elif op1 == 1: # bxl
        reg[B] = reg[B] ^ op2
    elif op1 == 2: # bst
        reg[B] = reg[op2] % 8
    elif op1 == 3: # jnz
        if reg[A] != 0:
            pc = op2-2
    elif op1 == 4: # bcx
        reg[B] ^= reg[C]
    elif op1 == 5: # out
        out.append(reg[op2] % 8)
    elif op1 == 6: # bdv
        reg[B] = reg[A] // 2 ** reg[op2]
    elif op1 == 7: # cdv
        reg[C] = reg[A] // 2 ** reg[op2]
    pc += 2
print(out)