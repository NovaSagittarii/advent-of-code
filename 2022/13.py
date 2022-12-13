import sys
lines = [line.strip() for line in sys.stdin]

def compare(a, b):
    if type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            res = compare(a[i], b[i])
            if res != None: return res
        if len(a) < len(b): return True
        if len(a) > len(b): return False
    elif type(a) == int and type(b) == int:
        if a < b: return True
        if a > b: return False
    else:
        return compare([a], b) if type(a) == int else compare(a, [b])
    return None
def comparator(a, b):
    res = compare(a, b)
    if res == None: return 0
    return 1 if res else -1
acc = 0
index = 1
for i in range(len(lines))[::3]:
    a, b = map(eval, lines[i:i+2])
    res = compare(a, b)
    if res == True: acc += index
    index += 1
print(acc)

def bubbleSort(arr, compare):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if not compare(arr[j], arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return


l = list(map(eval, filter(None, lines)))
l.extend([[[2]], [[6]]])
print(l)
# from functools import cmp_to_key
# l.sort(key=cmp_to_key(comparator)) #why doesnt this work??
bubbleSort(l, compare)
print(l)
l = list(map(str, l))
a = l.index("[[2]]")+1
b = l.index("[[6]]")+1
print(a*b)