import math
import sys
lines = [l for l in sys.stdin]

import time    
epoch_time = time.time()

directionText = "^v<>"
directions = [ [(i,-1) for i in range(-1,2)], [(i,1) for i in range(-1,2)], [(-1,i) for i in range(-1,2)], [(1,i) for i in range(-1,2)] ]
surround = set(x for y in directions for x in y)

h = len(lines)
w = len(lines[0])
d = w*4
wo = d//2

def ke(x, y, idk=None):
	if x+wo < 0: print("x underflow")
	if x+wo > d: print("x overflow")
	return y*d+(x+wo)
def unke(k):
	xwo = k % d
	x = xwo - wo
	y = k // d
	return (x, y)

elfpos = {}
elves = []
for y, line in enumerate(lines):
	for x, c in enumerate(line):
		if c == '#':
			elfpos[ke(x,y)] = True
			elves.append([x, y, 0])

# print(elves)

t = 0
completed = False
while not completed:
	completed = True
	reqs = {}
	# grid = [[' ' for i in range(d)] for i in range(2*h)]
	# for x,y,do in elves:
	# 	grid[y+h//3][x+wo] = '#'

	for elf in elves:
		x,y,do = elf
		if sum(ke(x+dx,y+dy) in elfpos for dx,dy in surround) == 0: # no one around
			continue
		for di in range(len(directions)):
			di = (di+do+t)%len(directions)
			# elf[2] = di+1 # update offset ... dont
			checks = directions[di]

			direction = checks[1] # middle lol
			met = True
			for dx,dy in checks:
				if ke(x+dx,y+dy) in elfpos:
					met = False
					break
			if met:
				# grid[y+h//3][x+wo] = directionText[di]
				dx,dy = direction
				k = ke(x+dx,y+dy)
				if k in reqs: reqs[k] = -1
				else:
					reqs[k] = elf
				break
	# print("\n".join("".join(l) for l in grid), t)

	for k in reqs.keys():
		if reqs[k] == -1: continue
		new = k # x,y = unke(k)
		old = ke(*reqs[k])
		del elfpos[old]
		elfpos[k] = True
		reqs[k][0], reqs[k][1] = unke(k)
		completed = False # keeep on goin
	# if t > 2: break
	if t == 9:
		big = [x for x in elves[0]]
		small = [x for x in elves[0]]
		for elf in elves:
			for k in range(2):
				big[k] = max(big[k], elf[k])
				small[k] = min(small[k], elf[k])
		print( (big[0]-small[0]+1) * (big[1]-small[1]+1) - len(elves) )
	t += 1

# grid = [[' ' for i in range(d)] for i in range(2*h)]
# for x,y,do in elves:
# 	grid[y+h//3][x+wo] = '#'
# print("\n".join("".join(l) for l in grid))

print(t)


print("time taken", time.time()-epoch_time)