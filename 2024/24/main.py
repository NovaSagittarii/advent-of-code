import sys
lines = [line.strip() for line in sys.stdin]

swaptable = {}
def addswap(u, v):
    swaptable[u] = v
    swaptable[v] = u
addswap('z14', 'hbk')
addswap('z18', 'kvn')
addswap('z23', 'dbb')
addswap('tfn', 'cvh')

init = {}
dp = {}
defs = {}
lookup = {}
for line in lines:
    if ':' in line:
        k, v = line.split(': ')
        v = int(v)
        init[k] = v
    elif '->' in line:
        xy, z = line.split(' -> ')
        a, op, b = xy.split()
        z = swaptable.get(z, z)
        if a > b: # swap
            temp = a
            a = b
            b = temp
        defs[z] = (a, op, b)
        lookup[' '.join(defs[z])] = z

st = set()
def dfs(u):
    if u in init: return init[u]
    if u in dp: return dp[u]

    if u in st: raise Exception("Cycle")
    st.add(u)

    x, op, y = defs[u]
    x = dfs(x)
    y = dfs(y)
    if op == 'OR': ret = x | y
    elif op == 'AND': ret = x & y
    elif op == 'XOR': ret = x ^ y
    dp[u] = ret

    st.remove(u)
    return ret

for u in defs.keys(): dfs(u)
ans = ""
for u in sorted(defs.keys(), reverse=True):
    if u[0] == 'z':
        # print(u, dfs(u))
        ans += str(dfs(u))
print(int(ans, 2))

# huh there's only 300 wires
# anyways you know only x0 and y0 should affect z0
# in general xi/yi can only affect zj where j >= i
# what does a swap do??
# hmm well
# theres 4 output wires that arent part of an XOR for some reason...
for k,xyz in defs.items():
    x,y,z = xyz
    if k[0] == 'z':
        if y != 'XOR':
            print('err', k)

# anyways in an adder, you need
# for lowest:
# Z = X ^ Y
# C = X & Y
# anywhere in the middle
# Z = X + Y + carry (k)
# Z0 = X ^ Y
# C0 = X & Y
# Z = Z0 ^ k
# C = Z0 ^ k
# wait wat the hec do the OR's do??

# for k,xyz in defs.items():
#     x,y,z = xyz
#     if y == 'XOR' and x[0]+z[0] in ['xy', 'yx']:
#         # print(x,y,z)
#         if k[0] != 'z':
#             print(k, xyz)
"""
x00 XOR y00 -> z00 # sum of xy
x00 AND y00 -> jfw # carry c00
y01 XOR x01 -> gnj # sum of xy
jfw XOR gnj -> z01 # sum of xy+c00
gnj AND jfw -> spq # carry c01 (of xy+c00)
"""
# ^[xy](\d\d) AND [xy]\1
# ok so a quick check reveals all the XOR are set up right (probably)
# and AND also looks set up correctly (input wise)

# aight so
"""
sjr OR  tck -> z14 is DEFINITELY wrong because
y14 AND x14 -> tck(carry bit)
y14 XOR x14 -> dfb (oh this should be z14)
bfn AND dfb -> sjr
dfb XOR bfn -> hbk (wait this should be z14)

y18 AND x18 -> z18(carry bit) is ALSO definitely wrong
x18 XOR y18 -> grp ; this would be better for z18
grp XOR fgr -> kvn ; jk this is better for z18 (fgr a prevcarry probably)
dvw AND rpg -> z23
dvw XOR rpg -> dbb ; probably swap this?? wait no that's not right
y23 XOR x23 -> rpg ; uhh swapping rpg<->z23 doesn't seem right
hey wait a minute are some of them unused?? (no)

qqt is the prevcarry
drc XOR qqt -> z44 ; drc/qqt is half-sum and prevcarry? half-sum
drc AND qqt -> cjf ; and this the full-carry

x44 XOR y44 -> drc ; this is the half-sum
x44 AND y44 -> pfk ; this is the half-carry

cjf OR  pfk -> z45  ; err... this should be the carry (x44 + y44 + c44 >= 2)
"""
# actually finding 2 pairs makes the problem solvable (200 choose 4 ~ 6e7)

def swap(u, v):
    temp = defs[u]
    defs[u] = defs[v]
    defs[v] = temp
# swap('z14', 'dfb') # uhh this introduces a cycle...
# swap('z14', 'hbk')
# swap('z18', 'kvn')
candidate = [u for u in defs.keys() if u not in 
    [
        'z14', 'z18', 'hbk', 'kvn',
    ]
]

zkeys = sorted([u for u in defs.keys() if u[0]=='z'], reverse=True)
def test(x, y):
    x &= (1 << 45) - 1
    y &= (1 << 45) - 1
    z = x + y
    
    for i in range(45):
        init['x'+str(i).zfill(2)] = 1 if x & (1 << i) else 0
        init['y'+str(i).zfill(2)] = 1 if y & (1 << i) else 0

    dp.clear()
    st.clear()
    ans = ""
    try:
        for u in zkeys: ans += str(dfs(u))
    except:
        # print("failed")
        return False
    # print(int(ans,2), z)

    return int(ans, 2) == z
print(test(123, 124))

def attempt(a, b, c, d):
    swap(a, b)
    swap(c, d)
    p = (1 << 42) - 1
    q = 672384
    tests = [
        (p, p), (q, q), (p, 0), (4724, 7429), (0, 0)
    ]
    for x, y in tests:
        if not test(x, y):
            return False
    print(a,b,c,d)
    return True
from itertools import combinations
i = 0
# w = len(tuple(combinations(candidate, 4)))
for a, b, c, d in combinations(candidate, 4):
    break
    if i & 1023 == 1023: print(i)
    i += 1
    if attempt(a, b, c, d): break
    if attempt(a, c, b, d): break
    if attempt(a, d, b, c): break

def Lookup(p, op, q):
    k = " ".join([p, op, q])
    k2 = " ".join([q, op, p])
    if k not in lookup: return lookup[k2]
    return lookup[k]
for i in range(1, 45):
    i = str(i).zfill(2)
    xi = 'x'+i
    yi = 'y'+i
    zi = 'z'+i
    xay = Lookup(xi, 'AND', yi) # half-carry
    xxy = Lookup(xi, 'XOR', yi) # half-sum
    p, _, q = defs[zi]
    paq = Lookup(p, 'AND', q) # used in carry
    pxq = Lookup(p, 'XOR', q) # output bit
    # print(xi, yi, 'carry', Lookup(xay, 'OR', paq))

print(','.join(sorted(swaptable.keys())))