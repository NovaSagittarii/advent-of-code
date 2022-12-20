import math

import sys
lines = [l for l in sys.stdin]

ct = 0

arithmeticseqcache = {}
def arithmeticseq(x):
    if x in arithmeticseqcache: return arithmeticseqcache[x]
    if x <= 1: return 1
    res = x+arithmeticseq(x-1)
    arithmeticseqcache[x] = res
    return res;

def dfs(time, resource, bots, recipe, big=0):
    # print(time, resource, bots)
    global ct
    ct += 1
    # if ct % 100000 == 0: print(ct)
    ore,clay,obi,geo = resource
    if time <= 0: return geo
    # if geo + arithmeticseq(big) <= big: return geo # give up even if you could build orebots from now on every minute

    b1,b2,b3 = bots # b1,b2,b3,b4 = bots
    o1,o2,o3,c3,o4,c4 = recipe
    z1 = max(o1, o2, o3, o4) # high ore cost
    z2 = c3 # high clay cost
    z3 = c4 # high obi cost


    # decide to build orebot
    if b1*time+ore < time*z1:
    # if b1 > 0 and b1*time+ore < time*z1:
        dt = 1+max(0, math.ceil((o1-ore)/b1))
        big = max(big, dfs(time-dt, (ore+dt*b1 -o1,clay+dt*b2,obi+dt*b3,geo), (b1+1,b2,b3), recipe, big))

    # decide to build claybot
    if b2*time+clay < time*z2:
        dt = 1+max(0, math.ceil((o2-ore)/b1))
        big = max(big, dfs(time-dt, (ore+dt*b1 -o2,clay+dt*b2,obi+dt*b3,geo), (b1,b2+1,b3), recipe, big))

    # decide to build obibot
    if b3*time+obi < time*z3 and b2 > 0:
        dt = 1+max(0, math.ceil((o3-ore)/b1), math.ceil((c3-clay)/b2))
        big = max(big, dfs(time-dt, (ore+dt*b1 -o3,clay+dt*b2 -c3,obi+dt*b3,geo), (b1,b2,b3+1), recipe, big))

    # decide to build geobot
    if b3 > 0:
        dt = 1+max(0, math.ceil((o4-ore)/b1), math.ceil((c4-obi)/b3))
        big = max(big, dfs(time-dt, (ore+dt*b1 -o4,clay+dt*b2,obi+dt*b3 -c4,geo+max(0,(time-dt))), bots, recipe, big))

    # for buildnext in [nextbot] if nextbot else [0,1,2,3]:
    #     big = dfs(time-1, tuple(resource[i]+bots[i] for i in range(len(bots))), bots2, bots2, recipe, buildnext)
    # if ore >= o1 and b1*time+ore < time*z1: big = max(big, dfs(time, (ore-o1,clay,obi,geo), bots, (b1+1,b2,b3,b4), recipe, None))
    # if ore >= o2 and b2*time+clay < time*z2: big = max(big, dfs(time, (ore-o2,clay,obi,geo), bots, (b1,b2+1,b3,b4), recipe, None))
    # if ore >= o3 and clay >= c3 and b3*time+obi < time*z3: big = max(big, dfs(time, (ore-o3,clay-c3,obi,geo), bots, (b1,b2,b3+1,b4), recipe, None))
    # if ore >= o4 and obi >= c4: big = max(big, dfs(time, (ore-o4,clay,obi-c4,geo), bots, (b1,b2,b3,b4+1), recipe, None))
    # print(time,resource, bots)
    return big
    
qual = 0
for line in lines:
    l = line.split(' ')
    i = int(l[1][:-1])
    o1,o2,o3,c3,o4,c4 = [int(l[i]) for i in (6, 12, 18, 21, 27, 30)]
    val = dfs(24,(0,0,0,0),(1,0,0),(o1,o2,o3,c3,o4,c4))
    # print(o1,o2,o3,c3,o4,c4)
    # print(i, val, ct)
    qual += i*val
print(qual)

# qual = 0
qual = 1
for line in lines[:3]:
    l = line.split(' ')
    i = int(l[1][:-1])
    o1,o2,o3,c3,o4,c4 = [int(l[i]) for i in (6, 12, 18, 21, 27, 30)]
    val = dfs(32,(0,0,0,0),(1,0,0),(o1,o2,o3,c3,o4,c4))
    # print(o1,o2,o3,c3,o4,c4)
    print(i, val, ct)
    qual *= val
print(qual)