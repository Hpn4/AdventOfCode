from helper import grid_iterator

lines = open(0, "r").readlines()

acc = 0
acc2 = 0

def xmas(x, y, lines):
	c = 0

	for acc in grid_iterator(lines, x, y, step=4, acc=True, diag=True):
		p = ""

		for xx, yy in acc:
			p += lines[yy][xx]

		c += p == "XMAS"

	return c

def cross_mass(x, y, lines):
	if x + 2 >= len(lines[y]) or y + 2 >= len(lines):
		return 0
	
	a = ""
	b = ""

	for i in range(3):
		a += lines[y + i][x + i]
		b += lines[y + i][x + 2 - i]

	return a in ("MAS", "SAM") and b in ("MAS", "SAM")

for y in range(len(lines)):
	lines[y] = lines[y].strip()
	for x in range(len(lines[y])):
		acc += xmas(x, y, lines)
		acc2 += cross_mass(x, y, lines)

print("Part1:", acc)
print("Part2:", acc2)
