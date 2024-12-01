import sys
import math
import numpy as np

d_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# grid
# gridint
# lines
# sections
# no
def read(file, lines=False, grid=False, intgrid=False):
	f = open(file, "r")
	ret = []

	if lines:
		ret = [line.strip() for line in f.readlines()]

	if grid:
		ret = [[c for c in line.strip()] for line in f.readlines()]

	if intgrid:
		ret = [[int(x) for x in line.strip()] for line in f.readlines()]

	return ret, len(ret), len(ret[0])

# Return coordinate of a given char in the grid
def findGrid(grid, c):
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == c:
				return (x, y)

	return None

def doEachDir(grid, x, y, fun, check=True):
	w = len(grid)
	h = len(grid[0])

	for accX, accY in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
		x1 = x + accX
		y1 = y + accY

		if check and not (0 <= x < w and 0 <= y < h):
			continue

		fun(x1, y1)

# Return the product of the list l
def prod(l):
	acc = 1
	for i in l:
		acc *= i

	return acc

# Return the lcm (least common multiple) of all the elements of l
def lcms(l):
	acc = 1
	for i in l:
		acc = math.lcm(acc, i)

	return acc

def interp(xs, ys, x, deg=2):
	poly = np.polynomial.polynomial.polyfit(xs, ys, deg)

	return np.polynomial.polynomial.polyval(x, poly)

# Return the area and the perimeter
def area(points):
	pass
	# area += (x + prevX) * (y - prevY)
	# abs(area // 2) + p//2 + 1

# Z3 equation solver:
# x = Int('x'); s = Solver(); s.add(x > 3); s.check(); s.model()
# https://ericpony.github.io/z3py-tutorial/guide-examples.htm

# sympy Line2D, Line3D for intersection, parallel...

# networkx, igraph: 