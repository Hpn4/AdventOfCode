from collections import defaultdict

lines = [l.strip() for l in open(0, "r").readlines()]

an = defaultdict(list)
for y in range(len(lines)):
	for x in range(len(lines[0])):
		c = lines[y][x]

		if c != '.':
			an[c].append((x,y))

def bound(xx, yy, lines):
	return xx >= 0 and yy >= 0 and xx < len(lines[0]) and yy < len(lines)

p = set()
p2 = set()
def iter_grid(dx, dy, x, y, lines):
	xx = x + 2 * dx
	yy = y + 2 * dy
	if bound(xx, yy, lines):
		p.add((xx,yy))

	xx = x - dx
	yy = y - dy
	if bound(xx, yy, lines):
		p.add((xx,yy))

def iter_grid2(dx, dy, x, y, lines):
	p2.add((x,y))

	xx = x + dx
	yy = y + dy
	while bound(xx, yy, lines):
		p2.add((xx,yy))
		xx += dx
		yy += dy

	xx = x - dx
	yy = y - dy
	while bound(xx, yy, lines):
		p2.add((xx,yy))
		xx -= dx
		yy -= dy

for freq in an:
	pos = an[freq]

	for i in range(len(pos)):
		x, y = pos[i]
		for j in range(i + 1, len(pos)):
			xj, yj = pos[j]
			dx = x - xj
			dy = y - yj

			iter_grid(dx, dy, xj, yj, lines)
			iter_grid2(dx, dy, xj, yj, lines)

print("Part1:", len(p))
print("Part2:", len(p2))
