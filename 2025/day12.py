lines = open("input12.txt").readlines()

acc = 0
for line in lines:
	if ":" in line and "x" in line:
		dim, inds = line.split(":")

		h, w = [int(x) for x in dim.split("x")]
		inds = [int(x) for x in inds.split()]

		if sum(inds) * 9 <= h * w:
			acc += 1

print("Part1:", acc)