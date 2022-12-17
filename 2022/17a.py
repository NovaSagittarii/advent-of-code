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

j = 0
jet = lines[0]
grid = [[y==0 for i in range(WIDTH)] for y in range(10000)]
highest = 0

for i in range(2022):
    # if i % 100000 == 0: print(i/1000000000000*100)
    piece = pieces[i%len(pieces)]
    # for l in range(highest+1)[::-1]:
    #    print("".join('#' if x else ' ' for x in grid[l]))
    # print(i, len(piece), len(piece[0]))
    # if i == 4: break
    h = len(piece)
    w = len(piece[0])
    x = 2
    y = highest + 4
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
            break
        x, y = newx, newy
print(highest)
