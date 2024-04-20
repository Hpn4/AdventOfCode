import sys

lines = open(sys.argv[1], "r").readlines()

dirs = {'<': (-1, 0), '>': (1, 0), 'v': (0, 1), '^': (0, -1)}

part1 = 0
part2 = 0
for line in lines:
	# Part 1
	x0, y0 = 0, 0
	seen1 = set()
	seen1.add((x0, y0))

	# Part2
	x, y = 0, 0
	x1, y1 = 0, 0
	seen = set()
	seen.add((x, y))

	for i, c in enumerate(line):
		accX, accY = dirs[c]

		if i % 2 == 0:
			x += accX
			y += accY
			seen.add((x, y))
		else:
			x1 += accX
			y1 += accY
			seen.add((x1, y1))

		x0 += accX
		y0 += accY
		seen1.add((x0, y0))

	part1 += len(seen1)
	part2 += len(seen)

print("Part1:", part1)
print("Part2:", part2)