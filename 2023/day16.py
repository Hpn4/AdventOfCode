import sys

lines = open(sys.argv[1], "r").readlines()
lines = [[c for c in line.strip()] for line in lines]

w = len(lines[0])
h = len(lines)

move = {
	'/': {'right': 'up', 'down': 'left', 'left': 'down', 'up': 'right'},
	'\\': {'right': 'down', 'down': 'right', 'up': 'left', 'left': 'up'}
}

ors = {'left': (-1, 0), 'up': (0, -1), 'right': (1, 0), 'down': (0, 1)}

def move_beam(x, y, o, states, energized):
	accX, accY = ors[o]
	key = (x, y, o)

	while key not in states and x >= 0 and y >= 0 and x < w and y < h:
		energized.add((x,y))
		states.add(key)
		c = lines[y][x]

		if c in "/\\":
			o = move[c][o]
			accX,accY = ors[o]

		if c == '-' and o in ['up', 'down']:
			move_beam(x - 1, y, 'left', states, energized)
			o = 'right'
			accX,accY = ors[o]

		if c == '|' and o in ['left', 'right']:
			move_beam(x, y - 1, 'up', states, energized)
			o = 'down'
			accX,accY = ors[o]

		x += accX
		y += accY
		key = (x, y, o)

def do_move(x, y, o):
	energized = set()
	move_beam(x, y, o, set(), energized)

	return len(energized)

m = 0
# To right and to left
for y in range(h):
	m = max(m, do_move(0, y, 'right'))
	m = max(m, do_move(w - 1, y, 'left'))

# To up and to down
for x in range(w):
	m = max(m, do_move(x, 0, 'down'))
	m = max(m, do_move(x, h - 1, 'up'))

print("Part1:", do_move(0, 0, 'right'))
print("Part2:", m)	