import sys

lines = open(sys.argv[1], "r").readlines()
lines = [line.strip() for line in lines]

# Parsing time. Exctract the maximum wdith/depth and max height
m, lm = 0, 0
pos = []
for line in lines:
	s, e = line.split("~")

	xs, ys, zs = [int(x) for x in s.split(",")]
	xe, ye, ze = [int(x) for x in e.split(",")]

	m = max(m, xe, ye)
	lm = max(lm, ze)

	pos.append((xs, ys, zs, xe, ye, ze))

# Making them fall
ground = [[0 for _ in range(m + 1)] for _ in range(m + 1)]

for lvl in range(1, lm + 1):
	for i in range(len(pos)):
		xs, ys, zs, xe, ye, ze = pos[i]

		if zs != lvl:
			continue

		z = 0
		for x in range(xs, xe + 1):
			for y in range(ys, ye + 1):
				z = max(z, ground[y][x])

		ze = (ze - zs) + z + 1
		zs = z + 1

		for x in range(xs, xe + 1):
			for y in range(ys, ye + 1):
				ground[y][x] = ze

		pos[i] = (xs, ys, zs, xe, ye, ze)

# Count blocks just above or just below block
def count(block, down=False):
	xs, ys, zs, xe, ye, ze = block
	acc = []

	for xs1, ys1, zs1, xe1, ye1, ze1 in pos:
		if down and zs - 1 != ze1:
			continue

		if not down and zs1 != ze + 1:
			continue

		if xe1 < xs or ye1 < ys:
			continue

		if xs1 > xe or ys1 > ye:
			continue

		acc.append((xs1, ys1, zs1, xe1, ye1, ze1))

	return acc

## PART 2
# Count brick just above
part1 = 0
for block in pos:
	up = count(block)
	good = False

	if up == 0:
		good = True
	else:
		good = True
		for blk in up:
			if len(count(blk, True)) == 1:
				good = False

	if good:
		part1 += 1

# Build fall dico
fall = {}
for block in pos:
	up = count(block)

	down = [(blk, count(blk, True)) for blk in up]

	fall[block] = down

def listIn(a, b):
	for c in a:
		if c not in b:
			return False

	return True

part2 = 0
for i in range(len(pos)):
	falled = set()

	start = [pos[i]]
	while start:
		block = start.pop()
		falled.add(block)

		tofall = fall[block]

		for (block, l) in tofall:
			if listIn(l, falled):
				part2 += 1
				start.append(block)

print("Part1:", part1)
print("Part2:", part2)