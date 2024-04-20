import sys

lines = open(sys.argv[1], "r").readlines()

# Part1
part1 = 0
for line in lines:
	line = line.strip()

	if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
		continue

	nice = False
	voy = line[0] in "aeiou"
	for i in range(1, len(line)):
		voy += line[i] in "aeiou"
		if line[i] == line[i - 1]:
			nice = True

	if nice and voy >= 3:
		part1 += 1

# Part2
part2 = 0
for line in lines:
	line = line.strip()

	good = False
	for i in range(0, len(line) - 1):
		c = line[i] + line[i + 1]

		for v in range(i + 2, len(line) - 1):
			if line[v] + line[v + 1] == c:
				good = True

	if not good:
		continue
	good = False

	for i in range(0, len(line) - 2):
		if line[i] == line[i + 2]:
			good = True

	if good:
		part2 += 1

print(part2)

# 204 torp haut