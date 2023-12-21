import sys

lines = open(sys.argv[1], "r").readlines()
lines = [[c for c in line.strip()] for line in lines]

h = len(lines)
w = len(lines[0])

start = 0
for y in range(h):
	for x in range(w):
		if lines[y][x] == "S":
			start = (x, y)

def run(pos, prec, steps):
	for i in range(prec, steps):
		moved = set()

		for x,y in pos:
			for accX, accY in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
				x1 = x + accX
				y1 = y + accY

				if lines[y1 % h][x1 % w] != '#':
					moved.add((x1, y1))

		pos = moved

	return pos

pos = set([start])

def black_magic(n):
	s = (w - 1) // 2

	s0 = run(pos, 0, s)
	a0 = len(s0)

	s1 = run(s0, s, s + w)
	a1 = len(s1)

	s2 = run(s1, s + w, s + w * 2)
	a2 = len(s2)

	# Find poly: ax² + bx + c
	# Write down formula:
	# a0 = 0² + b * 0 + c
	# a1 = a + b + c
	# a2 = 4a + 2b + c
	#
	# Substract
	# a2 - 2a1 = 2a - c
	#
	# So:
	# c = a0
	# a = (a2 - 2a1 + c) / 2
	# b = a1 - a - c

	c = a0
	a = (a2 - 2 * a1 + c) // 2
	b = a1 - a - c

	# Construct poly and then evaluate
	return a * n * n + b * n + c

print("Part1:", len(run(pos, 0, 64)))
print("Part2:", black_magic(26501365//w))