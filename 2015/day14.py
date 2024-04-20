import sys
import re

lines = open(sys.argv[1], "r").readlines()
com = {}

for line in lines:
	km, time, rest = [int(x) for x in re.findall("\d+", line)]
	com[(km, time, rest)] = (False, 0, 0, 0)

for i in range(2503):
	d = 0
	for (km, time, rest), (resting, distance, acc, score) in com.items():
		if resting:
			acc += 1
			if acc >= rest:
				resting = False
				acc = 0
		else:
			acc += 1
			distance += km
			if acc >= time:
				resting = True
				acc = 0

		if distance > d:
			d = distance

		com[(km, time, rest)] = (resting, distance, acc, score)

	for (km, time, rest), (resting, distance, acc, score) in com.items():
		if distance == d:
			com[(km, time, rest)] = (resting, distance, acc, score + 1)

d, sc = 0, 0
for (_, _, _), (_, distance, _, score) in com.items():
	d = max(d, distance)
	sc = max(sc, score)

print("Part1:", d)
print("Part2:", sc)