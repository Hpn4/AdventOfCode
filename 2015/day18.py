import sys

lines = open(sys.argv[1], "r").readlines()
G = [[c for c in line.strip()] for line in lines]

h = len(G)
w = len(G[0])

def countN(G, x, y):
	acc = 0
	for accX in [-1, 0, 1]:
		for accY in [-1, 0, 1]:
			if accX == 0 and accY == 0:
				continue

			x1 = x + accX
			y1 = y + accY

			if 0 <= x1 < w and 0 <= y1 < h and G[y1][x1] == '#':
				acc += 1

	return acc

def cornerOn(G):
	G[0][0] = '#'
	G[0][-1] = '#'
	G[-1][0] = '#'
	G[-1][-1] = '#'

def solve(G, p2):
	if p2:
		cornerOn(G)

	for i in range(100):
		G2 = [['.']*w for _ in range(h)]

		for x in range(w):
			for y in range(h):
				c = countN(G, x, y)

				on = G[y][x] == '#'
				if on and (c == 2 or c == 3):
					G2[y][x] = '#'
				elif not on and c == 3:
					G2[y][x] = '#'

		G = G2
		if p2:
			cornerOn(G)

	# Count
	acc = 0
	for x in range(w):
		for y in range(h):
			if G[y][x] == '#':
				acc += 1

	return acc

print("Part1:", solve(G.copy(), False))
print("Part2:", solve(G, True))
