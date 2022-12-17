import sys
lines = [line.strip() for line in sys.stdin]

pieces = list(map(lambda x: [list(line) for line in x.split('\n')][::-1], ['####','''.#.
###
.#.''','''..#
..#
###''','''#
#
#
#''','''##
##''']))
# print(pieces)
# for piece in pieces: print("\n", \n".join(["".join(line) for line in piece]))

WIDTH = 7


def simulate(time):
    visited = {}
    j = 0
    jet = lines[0]
    grid = [[y==0 for i in range(WIDTH)] for y in range(1000)]
    highest = 0
    highestInc = 0
    highestInCol = [0 for y in range(WIDTH)]
    i = 0
    while i < time: # for i in range(time):
        piece = pieces[i%len(pieces)]
        # for l in range(highest+1)[::-1]:
        #    print("".join('#' if x else ' ' for x in grid[l]))
        # print(i, len(piece), len(piece[0]))
        # if i == 4: break
        h = len(piece)
        w = len(piece[0])
        x = 2
        y = highest + 4
        k = j*len(pieces)+(i%len(pieces))
        k2 = ",".join([str(min(1000, highest-x)) for x in highestInCol])
        if k not in visited: visited[k] = {}
        if k2 not in visited[k]: visited[k][k2] = (i, highest)
        
        else:
            # print("hey i've been here before", visited[k][k2])
            ci, ch = visited[k][k2]
            dh = highest - ch
            dt = i - ci
            mult = (time-i) // dt
            if mult > 0:
                highestInc = dh * mult
                i += dt * mult
                print("skipped to ", i, "h=", highestInc)
                continue
        if y+h >= len(grid):
            for _ in range(100):
                grid.append([y==0 for i in range(WIDTH)])
        while True:
            newx = x + (-1 if jet[j]=="<" else 1)
            # print(jet[j], end='')
            newy = y
            j = (j+1)%len(jet)
            if newx < 0 or newx+w > WIDTH: newx = x
            collided = False
            for pi in range(h):
                for pj in range(w):
                    if piece[pi][pj] == '#' and grid[pi+newy][pj+newx]:
                        collided = True
                        break
                if collided: break
            if collided: newx = x
            # print(newx, newy)
            newy -= 1
            # print(newx, newy)
            collided = False
            for pi in range(h):
                for pj in range(w):
                    if piece[pi][pj] == '#' and grid[pi+newy][pj+newx]:
                        collided = True
                        break
                if collided: break
            if collided:
                newy += 1 # undo falling
                for pi in range(h):
                    for pj in range(w):
                        if piece[pi][pj] == '#':
                            grid[pi+newy][pj+newx] = True
                            highest = max(highest, pi+newy)
                            highestInCol[pj+newx] = max(highestInCol[pj+newx], pi+newy)
                break
            x, y = newx, newy
        i += 1
    return highest + highestInc

print(simulate(2022))
print(simulate(1000000000000))