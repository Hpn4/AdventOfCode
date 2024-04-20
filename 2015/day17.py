import sys
from itertools import combinations

lines = open(sys.argv[1], "r").readlines()
nmbs = [int(x.strip()) for x in lines]

part1 = 0
minCount = -1
for i in range(3, len(nmbs)):
	for c in combinations(nmbs, i):
		if sum(c) == 150:
			part1 += 1

			if minCount == -1:
				minCount = i

part2 = 0
for c in combinations(nmbs, minCount):
	if sum(c) == 150:
		part2 += 1

print("Part1:", part1)
print("Part2:", part2)