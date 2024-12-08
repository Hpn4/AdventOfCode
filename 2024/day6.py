from collections import defaultdict
from helper import findGrid, DIRS

lines = open(0, "r").readlines()
lines = [[c for c in line.strip()] for line in lines]

# Start position
s_x, s_y = findGrid(lines, '^')

def run(x, y, lines):
	d = 3
	pos = defaultdict(int)
	pos[(x, y)] = d
	while True:
		xx = x + DIRS[d][0]
		yy = y + DIRS[d][1]

		if xx < 0 or yy < 0 or xx >= len(lines[0]) or yy >= len(lines):
			return len(pos), pos.keys()

		if lines[yy][xx] == "#":
			d = (d + 1) % 4
		else:
			x = xx
			y = yy

			key = (xx, yy)
			if key in pos and pos[key] == d:
				return -1, None
			else:
				pos[key] = d

acc, pos = run(s_x, s_y, lines)

acc2 = 0
for (x, y) in pos:
	if lines[y][x] != '.':
		continue

	lines[y][x] = '#'

	if run(s_x, s_y, lines)[0] == -1:
		acc2 += 1

	lines[y][x] = '.'

print("Part1:", acc)
print("Part2:", acc2)