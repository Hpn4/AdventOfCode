import sys
from z3 import *

lines = open(sys.argv[1], "r").readlines()

points = []
for line in lines:
	pos, vel = line.strip().split(" @ ")

	pos = [int(x) for x in pos.split(",")]
	vel = [int(x) for x in vel.split(",")]

	points.append((pos, vel))

# Thanks to wikipedia page on line-line-intersection
# I could have used sympy or sickit-spatial instead
def intersect(pos, vel, pos1, vel1):
	x0, y0, _ = pos
	x1, y1 = x0 + vel[0], y0 + vel[1]

	x2, y2, _ = pos1
	x3, y3 = x2 + vel1[0], y2 + vel1[1]

	d = (x0 - x1) * (y2 - y3) - (y0 - y1) * (x2 - x3)

	if d == 0: # Parallel
		return False, 0, 0

	a = (x0 * y1 - y0 * x1)
	b = (x2 * y3 - y2 * x3)

	px = (a * (x2 - x3) - (x0 - x1) * b) / d
	py = (a * (y2 - y3) - (y0 - y1) * b) / d

	if (px - x0) / (x0 - x1) > 0 or (px - x2) / (x2 - x3) > 0:
		return False, 0, 0

	return True, px, py

testMin = 200000000000000
testMax = 400000000000000

seen = set()
for i, (pos, vel) in enumerate(points):
	for j, (pos1, vel1) in enumerate(points):
		if i == j or (i, j) in seen or (j, i) in seen:
			continue

		g, x, y = intersect(pos, vel, pos1, vel1)

		if not g:
			continue

		if testMin <= x <= testMax and testMin <= y <= testMax:
			seen.add((i, j))

# Part2
n = 5 # Check for 5 intersections is enough
x, y, z, ax, ay, az = Ints('x y z ax ay az')
T = [Int(f'T{i}') for i in range(n)]

s = Solver()
for i in range(n):
	pos, vel = points[i]
	s.add(x + T[i]*ax == pos[0] + T[i]*vel[0])
	s.add(y + T[i]*ay == pos[1] + T[i]*vel[1])
	s.add(z + T[i]*az == pos[2] + T[i]*vel[2])

res = s.check()
m = s.model()

print("Part1:", len(seen))
print("Part2:", m.eval(x + y + z))