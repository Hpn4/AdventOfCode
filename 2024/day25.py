import sys

lines = open(sys.argv[1], "r").read().strip()

schemas = lines.split('\n\n')
keys = []
locks = []

for schema in schemas:
	acc = []

	lines = schema.split('\n')
	for i in range(len(lines)):
		lines[i] = lines[i].strip()

	key = lines[0][0] == "#"

	for x in range(len(lines[0])):
		accX = 0
		for y in range(len(lines)):
			accX += lines[y][x] == "#"

		acc.append(accX - 1)

	if key:
		keys.append(acc)
	else:
		locks.append(acc)

acc = 0
for key in keys:
	for lock in locks:
		good = True
		for i in range(len(lock)):
			if key[i] + lock[i] > 5:
				good = False

		if good:
			acc += 1

print("Part1:", acc)