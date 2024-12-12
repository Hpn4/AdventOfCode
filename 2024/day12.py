from collections import defaultdict
from helper import findGrid, DIRS

# line = open(0, "r").readlines()[0].strip()
lines = open(0, "r").readlines()
grid = [[c for c in line.strip()] for line in lines]

acc = 0
acc2 = 0
SEEN = set()

def are(s, s2, x, y, t, grid):
	if grid[y][x] != t or (x,y) in SEEN:
		return (0,0)

	p = 0
	SEEN.add((x,y))
	dd = []

	for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
		xx = x + dx
		yy = y + dy

		if not (0<=xx<len(grid[0]) and 0<=yy<len(grid)) or grid[yy][xx] != t:
			if dy != 0:
				s[y + dy * 0.1].append(x)

			if dx != 0:
				s2[x + dx * 0.1].append(y)
			p += 1
			continue

		if (xx,yy) not in SEEN:
			dd.append((xx,yy))

	area = 0
	for xx,yy in dd:
		(a,b) = are(s, s2, xx, yy, t, grid)
		p += a
		area += b

	return (p, area + 1)

def side(sides):
	size = 0
	for k in sides.keys():
		l = sorted(sides[k])
		size += 1
		for i in range(1, len(l)):
			# If there is a gap of more than 1 at the same (x/y) side
			# means there is another side at a (x/y) higher or below
			if abs(l[i] - l[i - 1]) >= 2:
				size += 1

	return size

for y in range(len(grid)):
	for x in range(len(grid[0])):
		if (x,y) in SEEN:
			continue

		side_y = defaultdict(list)
		side_x = defaultdict(list)

		p,a = are(side_y, side_x, x, y, grid[y][x], grid)
		sides = side(side_y) + side(side_x)

		acc += p * a
		acc2 += a * sides

print("Part1:", acc)
print("Part2:", acc2)