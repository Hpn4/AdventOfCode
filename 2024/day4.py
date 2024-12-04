from helper import DIAG_DIRS

lines = open(0, "r").readlines()

acc = 0
acc2 = 0

def xmas(x, y, lines):
	c = 0
	for dx, dy in DIAG_DIRS:
		p = ""
		
		for i in range(4):
			xx = x + dx * i
			yy = y + dy * i

			if xx < 0 or yy < 0 or xx >= len(lines[0]) or yy >= len(lines):
				break

			p += lines[yy][xx]

		if p == "XMAS":
			c += 1

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
