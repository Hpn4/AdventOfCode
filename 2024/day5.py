from collections import defaultdict

lines = open(0, "r").readlines()

acc = 0
acc2 = 0

rules = defaultdict(list)
order = []

for line in lines:
	line = line.strip()

	if "|" in line:
		a,b = map(int, line.split("|"))

		rules[a].append(b)
	elif line != "":
		order.append(list(map(int, line.split(","))))

def order_page(o):
	for i in range(len(o)):
		for j in range(i + 1, len(o)):
			# if o[j] must be before o[i] swap them
			if o[i] in rules[o[j]]:
				o[j], o[i] = o[i], o[j]

	return o[len(o) // 2]

for o in order:
	ok = True

	for i in range(len(o)):
		good = True
		for j in range(i + 1, len(o)):
			if o[i] in rules[o[j]]:
				good = False
				break

		if not good:
			ok = False
			break

	if ok:
		acc += o[len(o) // 2]
	else:
		acc2 += order_page(o)

print("Part1:", acc)
print("Part2:", acc2)