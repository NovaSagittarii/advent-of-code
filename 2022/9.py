import sys

lines = [line for line in sys.stdin]

def solve(chainLength):
    chain = [[0, 0] for i in range(chainLength)]
    
    # tgrid = [[" " for i in range(5)] for i in range(7)]
    tvisited = set()
    
    for line in lines:
        a, b = line.strip().split()
        b = int(b)
        
        dx, dy = 0, 0
        if a == "R": dx = 1
        elif a == "L": dx = -1
        elif a == "U": dy = -1
        elif a == "D": dy = 1
        else: print("WTF")
        
        # tgrid[ty+5][tx] = "#"
        tvisited.add(chain[-1][0]*2e5 + (chain[-1][1]+1e5))
        
        for _ in range(b):
            # print(a, i, "(", hx, hy, ") (", tx, ty, ")")
            # print(a, i, dx, dy)
            chain[0][0] += dx
            chain[0][1] += dy
            for i in range(1, len(chain)):
                hx,hy = chain[i-1]
                tx,ty = chain[i]
                offx = abs(hx-tx)
                offy = abs(hy-ty)
                if offx >= 2 or offy >= 2:
                    typeA = []
                    typeB = []
                    for dtx in range(-1,2):
                        for dty in range(-1,2):
                            nx = tx+dtx
                            ny = ty+dty
                            if abs(hx-nx) < 2 and abs(hy-ny) < 2:
                                if dtx == 0 or dty == 0: typeA.append((nx, ny))
                                else: typeB.append((nx, ny))
                    # print(len(typeA), len(typeB))
                    if len(typeA) and (offx == 0 or offy == 0): chain[i] = typeA[0]
                    else: chain[i] = typeB[0]
                # tgrid[ty+5][tx] = "#"
                tvisited.add(chain[-1][0]*2e5 + (chain[-1][1]+1e5))
    # print("\n".join(["".join(map(str, row)) for row in tgrid]))
    return len(tvisited)
    
print(solve(2), solve(10))