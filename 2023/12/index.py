import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

import functools

ans = 0
for line in lines:
    s, a = line.split()
    s = list("?".join([s]*5) + ".")
    a = arrayint(",".join([a]*5).split(','))
    @functools.cache
    def dfs(i, j, r):
        if i >= len(s):
            if j >= len(a):
                return 1
            return 0
        if j >= len(a):
            if s[i] == '#': return 0
            else: return dfs(i+1, j, r)
        if r > a[j]: return 0 # overcounted
        elif r == a[j]: # end of sequence
            if s[i] == '#': return 0
            return dfs(i+1, j+1, 0)
        else: # extend sequence
            if s[i] == '.': # cannot extend
                if 0 < r < a[j]: return 0 # didnt meet quota
                else: return dfs(i+1, j, r)
            if s[i] == '#': return dfs(i+1, j, r+1)            
            if s[i] == '?':
                can_end = dfs(i+1, j, 0) if r == 0 else 0
                return dfs(i+1, j, r+1) + can_end
    w = dfs(0, 0, 0)
    # print(w)
    ans += w
print(ans)