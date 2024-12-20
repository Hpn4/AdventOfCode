import sys
from helper import findGrid, DIRS

lines = open(sys.argv[1], "r").readlines()
grid = [[c for c in line.strip()] for line in lines]

sx,sy = findGrid(grid, "S")
ex,ey = findGrid(grid, "E")

def fillStart(x,y,ex,ey):
	PATH = []
	SEEN = set()
	while (x, y) != (ex, ey):
		PATH.append((x,y))
		SEEN.add((x,y))
		for dx, dy in DIRS:
			xx = dx + x
			yy = dy + y

			if (xx,yy) in SEEN:
				continue

			if grid[yy][xx] != "#":
				x,y = xx,yy
				break

	PATH.append((ex,ey))
	return PATH

path = fillStart(sx,sy,ex,ey)

acc = 0
acc2 = 0
for (i, A) in enumerate(path):
	sx,sy = A

	for (j, B) in enumerate(path):
		ex, ey = B

		d = abs(ex - sx) + abs(sy - ey)
		cost = len(path) - (i + (len(path) - j) + d)
		# len(path) - (i + len(path) - j + d)
		# len(path) -i -len(path) +j -d
		# j - i - d
		cost = j - i - d

		if d == 2 and cost >= 100:
			acc += 1
		if d < 21 and cost >= 100:
			acc2 += 1

print("Part1:", acc)
print("Part2:", acc2)