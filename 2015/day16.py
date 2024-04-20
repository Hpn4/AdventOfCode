import sys

ref = {
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1
}

lines = open(sys.argv[1], "r").readlines()
sues = []
for line in lines:
	sep = line.index(':')
	parts = line[sep + 2:].strip().split(', ')
	
	sue = {}
	for part in parts:
		k, v = part.split(": ")
		sue[k] = int(v)

	sues.append(sue)

for i in range(len(sues)):
	good = True
	for k, v in sues[i].items():
		if ref[k] != v:
			good = False
			break

	if good:
		print("Part1:", i + 1)
		break

for i in range(len(sues)):
	sue = sues[i]
	if "cats" in sue and sue["cats"] <= ref["cats"]:
		continue

	if "trees" in sue and sue["trees"] <= ref["trees"]:
		continue

	if "pomeranians" in sue and sue["pomeranians"] >= ref["pomeranians"]:
		continue

	if "goldfish" in sue and sue["goldfish"] >= ref["goldfish"]:
		continue

	good = True
	for k, v in sues[i].items():
		if k in ["cats", "trees", "pomeranians", "goldfish"]:
			continue

		if ref[k] != v:
			good = False
			break

	if good:
		print("Part2:", i + 1)
		break

# 14 quai joseph gillet