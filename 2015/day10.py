inp = "1113122113"

for j in range(50):
	prev = inp[0]
	i = 0
	new = ""

	for c in inp:
		if c == prev:
			i += 1
		else:
			new += str(i) + prev
			i = 1
			prev = c

	new += str(i) + prev
	inp = new

	if j == 39:
		print("Part1:", len(inp))
	elif j == 49:
		print("Part2:", len(inp))