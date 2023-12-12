import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

ans = 0
for line in lines:
    s, a = line.split()
    s = list(s + ".")
    a = arrayint(a.split(','))
    possible = set()
    def dfs(i, j, r, path):
        if i >= len(s):
            if j >= len(a):
                possible.add(path)
                return 1
            return 0
        if j >= len(a):
            if s[i] == '#': return 0
            else: return dfs(i+1, j, r, path+'.')
        if r > a[j]: return 0 # overcounted
        elif r == a[j]: # end of sequence
            if s[i] == '#': return 0
            return dfs(i+1, j+1, 0, path+'.')
        else: # extend sequence
            if s[i] == '.': # cannot extend
                if 0 < r < a[j]: return 0 # didnt meet quota
                else: return dfs(i+1, j, r, path+'.')
            if s[i] == '#': return dfs(i+1, j, r+1, path+'#')            
            if s[i] == '?':
                can_end = dfs(i+1, j, 0, path+'.') if r == 0 else 0
                return dfs(i+1, j, r+1, path+'#') + can_end
    ways = dfs(0, 0, 0, '')
    print(ways)
    # print(possible)
    w = len(possible)
    print(w)
    ans += w
print(ans)