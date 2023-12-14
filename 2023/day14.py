import sys

lines = open(sys.argv[1], "r").readlines()
lines = [[c for c in line.strip()] for line in lines]

h = len(lines)
w = len(lines[0])

def move_one(x, y, accX, accY):
	lines[y][x] = '.'

	prevX, prevY = x, y
	while x >= 0 and y >= 0 and x < w and y < h:
		if lines[y][x] in '#O':
			x = prevX
			y = prevY
			break

		prevX = x
		prevY = y
		x += accX
		y += accY

	y = max(0, min(y, h - 1))
	x = max(0, min(x, w - 1))

	lines[y][x] = 'O'

def create_set(lines):
	s = set()
	ha = 0

	for x in range(w):
		for y in range(h):
			if lines[y][x] == 'O':
				s.add((x,y))
				ha += (y * w + x) * h

	return s, ha

def score(s):
	return sum(h - y for _,y in s[0])

def move_all(p1 = False):
	i = 0

	# North
	for y in range(h):
		for x in range(w):
			if lines[y][x] == 'O':
				move_one(x, y, 0, -1)

	if (p1):
		i = score(create_set(lines))

	# West
	for x in range(w):
		for y in range(h):
			if lines[y][x] == 'O':
				move_one(x, y, -1, 0)

	# South
	for y in range(h - 1, -1, -1):
		for x in range(w):
			if lines[y][x] == 'O':
				move_one(x, y, 0, 1)

	# East
	for x in range(w - 1, -1, -1):
		for y in range(h):
			if lines[y][x] == 'O':
				move_one(x, y, 1, 0)

	return i

def already(states, s):
	for i in range(len(states)):
		if s[1] == states[i][1]:
			return i

	return -1

part1 = 0
states = [create_set(lines)]
base = 0
for i in range(1000000000):
	if i == 0:
		part1 = move_all(True)
	else:
		move_all()

	se = create_set(lines)
	j = already(states, se)

	if j > 0:
		base = (i, j)
		break

	states.append(se)

# base[0]: number of cycle when start looping
# base[1]: indices in the set tables of the start state of the loop
l = 1000000000 - base[1] # Substract init part of the looping cycle

# Calculate number of cycles in the loop
loopSize = base[0] - base[1] + 1

index = l % loopSize + base[1]

print("Part1:", part1)
print("Part2:", score(states[index]))