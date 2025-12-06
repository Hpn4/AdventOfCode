
lines = open("input6.txt").readlines()

op = lines[-1].strip()
op = op.split()

lines = lines[:-1]

probs = [[] for _ in range(len(op))]
for line in lines:
	line = line.strip()
	for i,a in enumerate(line.split()):
		probs[i].append(a)

def solve(probs):
	acc2 = 0
	for i in range(len(op)):
		oo = op[i]
		acc = 1 if oo == "*" else 0

		for a in probs[i]:
			if oo == "*":
				acc *= int(a)
			else:
				acc += int(a)

		acc2 += acc

	return acc2

print("Part1:", solve(probs))

# Part2
max_ = max([len(line) for line in lines])

probs = [[] for _ in range(len(op))]
j = 0
for i in range(max_):
	empty = True
	nmb = ""
	for line in lines:
		if i >= len(line):
			continue

		c = line[i]
		if c != " " and c != "\n":
			nmb += c
			empty = False

	if empty:
		j += 1
	else:
		probs[j].append(nmb)

print("Part2:", solve(probs))
