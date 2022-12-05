line = "42069"

pillars = [[] for i in range(10)]

things = []
while(line[1] != "1"):
	if(line != "42069"): things.append(line[1::4])
	line = input()
for obj in reversed(things):
	for i, c in enumerate(obj):
		if c != ' ':
			pillars[i].append(c)

print(pillars)

input() # empty

line = input()
while(line != ""):
	a,b,c = map(int, line.split()[1::2])
	b -= 1
	c -= 1
	toappend = []
	for i in range(a):
		toappend.append(pillars[b].pop())
	for x in reversed(toappend):
		pillars[c].append(x)
	line = input()

print("".join(list(map(lambda x:"" if len(x) == 0 else x[-1], pillars))))


