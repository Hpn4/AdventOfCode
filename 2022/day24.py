import re
from collections import defaultdict

lines = [x.strip() for x in open("te.txt").readlines()]

# Width and height
size = (len(lines[0]), len(lines))

# Gets a dict of all the blizzards
def getBlizzards(lines):
	# Blizzards direction
	dirs = {">":0, "v":1, "<":2, "^":3, "#":-1, ".":-1}

	blizzards = defaultdict(list)
	for (y, line) in enumerate(lines):
		for (x, c) in enumerate(line):
			d = dirs[c]
			if d != -1:
				blizzards[(x, y)].append(d)

	return blizzards

# Return true if we can move to x,y false otherwise
def canMoveTo(x, y, blizzards):

	# There is a blizzard where we want to go
	if (x, y) in blizzards:
		return False

	# Top line
	if y == 0:
		return x == 1 # Start or wall

	# Left line
	if x == 0:
		return False

	(width, height) = size

	if y < 0 or y >= height:
		return False

	# Bottom line
	if y == height - 1:
		return x == width - 2 # End or wall

	# Right line
	if x == width - 1:
		return False

	return True

def moveBlizzards(blizzards):
	(width, height) = size
	bl = defaultdict(list)

	for ((dx, dy), dirs) in blizzards.items():
		for d in dirs:
			x = dx
			y = dy
			if d == 0:
				x += 1
				if x == width - 1:
					x = 1
			elif d == 1:
				y += 1
				if y == height - 1:
					y = 1
			elif d == 2:
				x -= 1
				if x == 0:
					x = width - 2
			else:
				y -= 1
				if y == 0:
					y = height - 2

			bl[(x, y)].append(d)

	return bl

end = (size[0] - 2, size[1] - 1)

best = [float('inf'), None]
freed = [0, 0, 0]
seen = set()
# 1 : 326
def getBest(x, y, blizzards, steps, end, mm):
	if (x, y) == end:
		best[0] = min(steps, best[0])
		best[1] = blizzards
		return steps

	if steps >= best[0] or steps > mm: # 900
		freed[0] += 1
		return float('inf')

	label = (x, y, steps)
	if label in seen:
		freed[1] += 1
		return float('inf')

	# Distance de manhattan entre ou on est et le point final
	if steps + abs(x - end[0]) + abs(y - end[1]) >= best[0]:
		freed[2] += 1
		return float('inf')

	seen.add(label)

	bl = moveBlizzards(blizzards)
	m = float('inf')

	if canMoveTo(x + 1, y, bl):
		m = min(m, getBest(x + 1, y, bl.copy(), steps + 1, end, mm))

	if canMoveTo(x, y + 1, bl):
		m = min(m, getBest(x, y + 1, bl.copy(), steps + 1, end, mm))

	if canMoveTo(x - 1, y, bl):
		m = min(m, getBest(x - 1, y, bl.copy(), steps + 1, end, mm))

	if canMoveTo(x, y - 1, bl):
		m = min(m, getBest(x, y - 1, bl.copy(), steps + 1, end, mm))

	if canMoveTo(x, y, bl):
		m = getBest(x, y, bl.copy(), steps + 1, end, mm) # Wait

	return m

blizzards = getBlizzards(lines)

# Partie 1
getBest(1, 0, blizzards, 1, end, 340)
p1 = best[0] - 1
print("Aller", best[0] - 1)

# Partie 2
seen = set()
best[0] = float('inf')
getBest(end[0], end[1], best[1], 1, (1, 0), 350)
p2 = p1 + best[0] - 1
print("Retour", best[0] - 1)

seen = set()
best[0] = float('inf')
getBest(1, 0, best[1], 1, end, 330)
p2 += best[0] - 1
print("De nouveau", best[0] - 1)

print("Partie 1: " + str(p1))
print("Partie 2:" + str(p2))

# 327 too high