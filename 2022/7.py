input() # dump % cd /

files = {}
locationstack = [files]

prev = None
while True:
    try:
        line = prev or input()
        prev = None
        a, cmd, arg = (line + " ?").split()[:3]
        if cmd == "cd":
            if arg == "..":
                locationstack.pop()
            elif arg == "/":
                locationstack = [files]
            else:
                newLocation = {}
                locationstack[-1][arg] = newLocation
                locationstack.append(newLocation)
        elif cmd == "ls":
            location = locationstack[-1]
            while True:
                try:
                    prev = input()
                    a, b = prev.split()
                    # print(a,b)
                    if a == "$": break
                    else: prev = None # clear since we process
                    if a == "dir":
                        location[b] = {}
                    else:
                        location[b] = int(a)
                except Exception:
                    break
    except Exception:
        break


totalspace = 70000000
emptyneeded = 30000000

# print(files)
smallFilesSum = 0
smallDirectory = 7829347892342

def explore(files):
    global totalspace
    global emptyneeded
    global smallDirectory
    global smallFilesSum
    total = 0
    for filename in files:
        file = files[filename]
        if type(file) == dict:
            total += explore(file)
        else:
            total += file
    if total <= 100000:
        smallFilesSum += total
    # files["__SIZE__"] = total
    if totalspace+total >= emptyneeded:
        smallDirectory = min(smallDirectory, total)
    return total
usedspace = explore(files)
totalspace -= usedspace

smallDirectory = 789432798424
explore(files)
print(usedspace, smallFilesSum)
print(smallDirectory)
# print(files)



    
    
    