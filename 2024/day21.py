import sys

DD = {(1,0):'>', (-1,0):'<', (0,1):'v', (0,-1):'^'}
PADD = {'7':(0,0), '8':(1, 0), '9': (2,0), '4':(0,1), '5':(1, 1), '6': (2,1),
	'1':(0,2), '2':(1, 2), '3': (2, 2), '0':(1, 3), 'A': (2,3),'^': (1,0), 'a':(2,0), '<': (0,1), 'v':(1,1), '>': (2,1)}

lines = open(sys.argv[1], "r").readlines()

def moves_set(x, y, dx, dy, robs):
	ax = -1 if dx < x else 1
	ay = -1 if dy < y else 1

	if x != dx or y != dy:
		x_first = [x, y, ""]
		y_first = [x, y, ""]

		# X first
		while x_first[0] != dx:
			if x_first[0] + ax == 0 and x_first[1] == robs:
				break
			x_first[0] += ax
			x_first[2] += DD[(ax,0)]

		while x_first[1] != dy:
			x_first[1] += ay
			x_first[2] += DD[(0,ay)]

		while x_first[0] != dx:
			x_first[0] += ax
			x_first[2] += DD[(ax,0)]

		# Y first
		while y_first[1] != dy:
			if y_first[0] == 0 and y_first[1] + ay == robs:
				break
			y_first[1] += ay
			y_first[2] += DD[(0,ay)]

		while y_first[0] != dx:
			y_first[0] += ax
			y_first[2] += DD[(ax,0)]

		while y_first[1] != dy:
			y_first[1] += ay
			y_first[2] += DD[(0,ay)]

		return [x_first[2] + "a", y_first[2] + "a"]

	return "a"

SEEN = dict()
def shortest(code, lim, depth = 0):
	key = (code, depth, lim)

	if key in SEEN:
		return SEEN[key]

	first = depth == 0
	x,y = (2, 3 if first else 0)
	acc = 0

	for c in code:
		dx,dy = PADD[c]
		moves = moves_set(x, y, dx, dy, 3 if first else 0)

		if depth == lim:
			acc += len(moves[0])
		else:
			acc += min(shortest(move, lim, depth + 1) for move in moves)

		x,y = dx, dy

	SEEN[key] = acc

	return acc

acc = 0
acc2 = 0

for code in lines:
	code = code.strip()
	res = int(code[:3])

	acc += shortest(code, 2) * res
	acc2 += shortest(code, 25) * res

print("Part1:", acc)
print("Part2:", acc2)