import sys
lines = [line.strip() for line in sys.stdin]

arrayint = lambda arr: list(int(x) for x in arr)

cards = []
for line in lines:
	hand, val = line.split()
	val = int(val)
	
	real_hand = []
	d = {}
	cti = {
		'T': 10,
		'J': 11,
		'Q': 12,
		'K': 13,
		'A': 14,
	}
	for c in hand:
		if c not in d: d[c] = 0
		d[c] += 1
		if c.isdigit():
			real_hand.append(int(c))
		else:
			real_hand.append(cti[c])
	
	freq = sorted(d.values(), reverse=True)
	# print(freq)
	power = -1
	if freq[0] == 5: power = 5
	elif freq[0] == 4: power = 4
	elif freq[0] == 3 and freq[1] == 2: power = 3
	elif freq[0] == 3: power = 2
	elif freq[0] == 2 and freq[1] == 2: power = 1
	elif freq[0] == 2: power = 0
	else: power = -1

	cards.append((power, real_hand, hand, val))
cards.sort()
# print(cards)
ans = 0
for i, s in enumerate(cards):
	p, rh, h, v = s
	ans += (i+1)*v
print(ans)