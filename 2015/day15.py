import sys
import re

lines = open(sys.argv[1], "r").readlines()

recipes = []
for line in lines:
	x = [int(x) for x in re.findall("-?\d+", line)]
	recipes.append(x)

def evaluate(p2, recipes, x):
	acc = 1
	# Calculate colories
	if p2:
		cal = 0
		for j in range(len(recipes)):
			cal += recipes[j][-1] * x[j]
		if cal != 500:
			return 0

	for i in range(4):
		s = 0
		for j in range(len(recipes)):
			s += recipes[j][i] * x[j]

		if s <= 0:
			return 0
		acc *= s

	return acc

def solve(p2):
	d = 0
	for i in range(100):
		for j in range(100 - i):
			for k in range(100 - i - j):
				xs = [i, j, k, 100 - i - j - k]
				d = max(d, evaluate(p2, recipes, xs))

	return d

print("Part1:", solve(False))
print("Part2:", solve(True))
