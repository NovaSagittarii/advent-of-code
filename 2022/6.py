s = input()

for i in range(4,len(s)+1):
    t = s[i-4:i]
    # print(i, t, set(list(t)))
    if(len(set(list(t))) == 4):
        print(i)
        break

for i in range(14,len(s)+1):
    t = s[i-14:i]
    # print(i, t, set(list(t)))
    if(len(set(list(t))) == 14):
        print(i)
        break