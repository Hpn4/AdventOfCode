import sys

line = open(sys.argv[1], "r").read().strip()

part1, part2 = 0, 0
for (i, c) in enumerate(line):
	part1 += {'(': 1, ')': -1}[c]

	if part1 == -1 and part2 == 0:
		part2 = i + 1

print("Part1:", part1)
print("Part2:", part2)