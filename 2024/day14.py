from collections import defaultdict
import sys

lines = open(sys.argv[1], "r").readlines()

w, h = 101, 103
robots = []
quad = [0,0,0,0]
for line in lines:
	line = line.strip()
	p,v = [[int(x) for x in part[2:].split(",")] for part in line.split()]

	robots.append((p,v))

	x = (p[0] + v[0] * 100) % w
	y = (p[1] + v[1] * 100) % h

	if x < w // 2 and y < h // 2:
		quad[0] += 1
	elif x > w // 2 and y < h // 2:
		quad[1] += 1
	elif x < w // 2 and y > h // 2:
		quad[2] += 1
	elif x > w // 2 and y > h // 2:
		quad[3] += 1

acc = 1
for i in quad:
	acc *= i

def is_tree_(robots):
	max_ad = 0
	for y in range(h):
		adj = 0
		for x in range(1, w):
			if (x,y) in robots and (x-1,y) in robots:
				adj += 1
		max_ad = max(adj, max_ad)

	if max_ad < 7:
		return False
	for y in range(h):
		s = ""
		for x in range(w):
			if (x,y) in robots:
				s += "#"
			else:
				s += "."
		print(s)
	return True

i = 0
is_tree = False
while not is_tree:
	is_tree = True
	rob = set()
	for j in range(len(robots)):
		p,v = robots[j]

		px = ((p[0] + v[0]) % w, (p[1] + v[1]) % h)
		robots[j] = (px, v)

		if px in rob:
			is_tree = False

		rob.add(px)

	is_tree = is_tree and is_tree_(rob)
	i += 1

print("Part1:", acc)
print("Part2:", i)
