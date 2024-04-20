import sys

lines = open(sys.argv[1], "r").readlines()

part1 = 0
part2 = 0
for line in lines:
	l,w,h = [int(x) for x in line.strip().split('x')]

	p1 = l * w
	p2 = w * h
	p3 = h * l

	part1 += 2 * (p1 + p2 + p3) + min(p1, p2, p3)

	part2 += l * w * h + 2 * min(l + w, w + h, h + l)

print(part1)
print(part2)