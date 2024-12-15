from collections import defaultdict
import sys
from helper import findGrid

movs = {'>':(1, 0), 'v':(0,1), '<':(-1, 0), '^':(0,-1)}
DD = {'[': +1, ']':-1}
conv = {'.': '..', '#':'##', 'O': '[]', '@': '@.'}

lines = open(sys.argv[1], "r").read()

grids, order = lines.split("\n\n")
order = order.replace("\n", "").strip()

def can_move(s, grid, x, y, dy):
	c = grid[y][x]
	if c == "#":
		return False

	if c == "[" or c == "]":
		s.append((x,y,c))
		
		return can_move(s, grid, x, y + dy, dy) and can_move(s, grid, x + DD[c], y + dy, dy)

	return c == "."

def move_robot2(grid, x, y, d):
	dx,dy = d
	sx = x
	sy = y

	# Vertical
	if dy != 0:
		s = []
		if (can_move(s, grid, x, y, dy)):
			s = sorted(s, key = lambda x : x[1], reverse=dy == 1)
			for x,y,c in s:
				grid[y][x] = '.'
				grid[y][x + DD[c]] = '.'

				if c == "[":
					grid[y + dy][x] = '['
					grid[y + dy][x + 1] = ']'
				else:
					grid[y + dy][x - 1] = '['
					grid[y + dy][x] = ']'

			return True

		return False


	# Horizontal:
	s = []
	while grid[y][x] == "[" or grid[y][x] == "]":
		if grid[y][x] == "[":
			s.append((x,y))
		x += dx
		y += dy
	s = sorted(s, key = lambda x : x[0], reverse=dx == 1)

	if grid[y][x] == "#":
		return False

	for x,y in s:
		grid[y][x] = "."
		grid[y][x + 1] = "."
		grid[y][x + dx + 1] = "]"
		grid[y][x + dx] = "["

	return True

def move_robot1(grid, x, y, d):
	dx,dy = d
	sx = x
	sy = y

	while grid[y][x] == "O":
		x += dx
		y += dy

	if grid[y][x] == "#":
		return False

	grid[y][x] = "O"
	grid[sy][sx] = "."

	return True

def solve(x, y, grid, order):
	for c in order:
		dx,dy = movs[c]

		xx,yy = x + dx, y + dy

		if grid[yy][xx] == "#":
			continue

		move = True
		if grid[yy][xx] == "[" or grid[yy][xx] == "]":
			move = move_robot2(grid, xx, yy, (dx, dy))

		if grid[yy][xx] == "O":
			move = move_robot1(grid, xx, yy, (dx, dy))

		if move:
			grid[y][x] = "."
			x = xx
			y = yy
			grid[y][x] = "@"

	acc = 0
	for y in range(1, len(grid) - 1):
		for x in range(1, len(grid[0]) - 1):
			if grid[y][x] == "[" or grid[y][x] == "O":
				acc += 100 * y + x

	return acc

grid = [[c for c in line.strip()] for line in grids.split("\n")]
x,y = findGrid(grid, "@")

print("Part1:", solve(x, y, grid, order))

grid = []
for line in grids.split("\n"):
	row = []
	for c in line.strip():
		for d in conv[c]:
			row.append(d)
	grid.append(row)

x,y = findGrid(grid, "@")

print("Part2:", solve(x, y, grid, order))