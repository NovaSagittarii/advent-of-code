import sys
lines = [line.strip() for line in sys.stdin]

DIGITS = "0123456789"

a = lines
n = len(lines)
m = len(lines[0])

ans = 0
for i in range(n):
    acc = ""
    sj = -1
    for j in range(m):
        is_digit = a[i][j] in DIGITS
        if is_digit: # append
            if sj < 0: sj = j
            acc += a[i][j]
        if (not is_digit or j == m-1) and sj >= 0:
            # search for nearby
            ok = False
            for ni in range(i-1, i+2):
                for nj in range(sj-1, j+1):
                    if 0 <= ni < n and 0 <= nj < m and a[ni][nj] != '.' and a[ni][nj] not in DIGITS:
                        ok = True
            if ok:
                ans += int(acc)
                # print(acc)
            # reset
            acc = ""
            sj = -1
print(ans)