
lines = open('input5.txt').read()

fresh, ids = lines.split("\n\n")

ids = [i.strip() for i in ids.split("\n")]
ids = ids[:-1]
ids = [int(i) for i in ids]

ranges = []
for line in fresh.split("\n"):
	line = line.strip()
	if len(line) == 0:
		continue

	a,b = line.split("-")
	ranges.append((int(a), int(b)))

acc = 0
for id_ in ids:
	spoiled = True
	for a,b in ranges:
		if a <= id_ <= b:
			spoiled = False
			break

	if not spoiled:
		acc += 1

print("Part1:", acc)

def find_range(a, b, i_):
	for i in range(len(ranges)):
		if i == i_:
			continue
		a_, b_ = ranges[i]

		if a <= a_ <= b or a_ <= a <= b_:
			return i

	return None

def merge(ranges):
	merged = False
	while True:
		merged = False

		# Part 2 compress ranges
		i = 0
		while i < len(ranges):
			a,b = ranges[i]

			j = find_range(a, b, i)

			if j is None:
				i += 1
				continue

			# Merge
			a_, b_ = ranges[j]
			merged = True

			min_ = min(min(b, b_), min(a, a_))
			max_ = max(max(b, b_), max(a, a_))
			ranges[i] = (min_, max_)

			del ranges[j]
			i += 1

		if not merged:
			return ranges

ranges = merge(ranges)

acc = 0
for a,b in ranges:
	acc += b - a + 1

print("Part2:", acc)