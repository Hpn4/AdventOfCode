import sys

lines = open(sys.argv[1], "r").read()

def hash_a(s):
	ac = 0
	for c in s:
		ac += ord(c)
		ac = (ac * 17) % 256

	return ac

def get_index(block, st):
	for bi,c in enumerate(block):
		if c[0] == st:
			return bi

	return -1

part1 = 0
d = [[] for x in range(256)]
for part in lines.split(','):
	part1 += hash_a(part)

	if part.endswith("-"):
		p = part[:-1]
		block = d[hash_a(p)]

		i = get_index(block, p) # Delete if exit
		if i >= 0:
			del block[i]
	else:
		st,slot = part.split("=")
		block = d[hash_a(st)]
		comb = (st, int(slot))

		# Update value if present or add at the end
		i = get_index(block, st)
		if i >= 0:
			block[i] = comb
		else:
			block.append(comb)

part2 = 0
for bi,block in enumerate(d):
	for ci,c in enumerate(block):
		part2 += (bi + 1) * (ci + 1) * c[1]

print("Part1:", part1)
print("Part2:", part2)