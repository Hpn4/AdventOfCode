import sys
from collections import deque

lines = open(sys.argv[1], "r").readlines()
lines = [[c for c in line.strip()] for line in lines]

h = len(lines)
w = len(lines[0])

dirs = {'<': (-1, 0), 'v': (0, 1), '>': (1, 0)}

def solve(part1):
	Q = deque()
	Q.append((1, 0, 0, set()))

	seen = {}

	d = 0
	while Q:
		x, y, a, s = Q.popleft()

		if (x, y) in s:
			continue

		toMove = []
		while True:
			toMove.clear()
			s.add((x, y))

			if part1:
				c = lines[y][x]
				if c in dirs:
					accX, accY = dirs[c]
					x += accX
					y += accY
					a += 1
					continue

			for accX, accY in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
				x1 = x + accX
				y1 = y + accY

				if not (0 <= x1 < w and 0 <= y1 < h):
					continue

				c = lines[y1][x1]
				if c == '#' or (x1, y1) in s:
					continue

				if part1 and ((accX == -1 and c == '>') or (accX == 1 and c == "<") or (accY == -1 and c == 'v')):
					continue

				toMove.append((x1, y1))

			if len(toMove) == 0:
				if y == h - 1 and x == w - 2:
					if a > d:
						d = a
						#print("New", d)
				break
			elif len(toMove) == 1:
				x, y = toMove[0]
				a += 1
			else:
				break

		if len(toMove) > 1:
			for x1, y1 in toMove:
				if (x1, y1) in seen and seen[(x1, y1)] > a + 105: # Increase this value if your solution is not right
					continue

				seen[(x1, y1)] = a + 1
				Q.append((x1, y1, a + 1, s.copy()))

	return d

print("Part1:", solve(True))
print("Part2:", solve(False))