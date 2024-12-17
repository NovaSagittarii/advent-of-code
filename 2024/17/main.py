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

regA = int(A[0].split()[-1])
code = tuple(map(int, A[-1].split()[-1].split(',')))

def run(a):
    reg = [0, 1, 2, 3, a, 0, 0]
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
            # return out
            # if len(out) > len(code): return False
        elif op1 == 6: # bdv
            reg[B] = reg[A] // 2 ** reg[op2]
        elif op1 == 7: # cdv
            reg[C] = reg[A] // 2 ** reg[op2]
        pc += 2
    return tuple(out)

print(run(0o6017))
# for i in range(1000000): run(i)

sz = 16
curr = [0]
for d in reversed(range(16)):
    next = []
    for u in curr:
        for j in range(8):
            v = u*8 + j
            res = run(v)
            ok = True
            # print(res, code, v)
            if res == code:
                print(v)
            for i, x in enumerate(res):
                if x != code[i+len(code)-len(res)]:
                    ok = False
            if ok:
                next.append(v)
    curr = next


