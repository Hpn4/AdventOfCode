import sys

lines = open(sys.argv[1], "r").readlines()

O = {'x': 0, 'm': 1, 'a': 2, 's': 3}
H = {}
i = 0
for line in lines:
	if line == '\n':
		break
	name, part = line[:-2].split('{')

	L = []
	for calc in part.split(','):
		if ':' in calc:
			cond, goto = calc.split(':')

			if '<' in cond:
				var, num = cond.split('<')
				L.append((0, O[var], int(num), goto))
			else:
				var, num = cond.split('>')
				L.append((1, O[var], int(num), goto))
		else:
			L.append((2, 0, 0, calc))

	H[name] = L
	i += 1

def workflow(n, name):
	while name != 'R' and name != 'A':
		for (lower, index, ope, next_name) in H[name]:
			if lower == 2 or (lower == 0 and n[index] < ope) or (lower == 1 and n[index] > ope):
				name = next_name
				break

	return name

part1 = 0
for line in lines[i + 1:]:
	line = line.strip()[1:-1]

	n = [int(p.split('=')[1]) for p in line.split(',')]
	if workflow(n, "in") == 'A':
		part1 += sum(n)

print("Part1:", part1)

# Part2
part2 = 0
n = [("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)])]
while n:
	name, l = n.pop()

	if name == 'R':
		continue # Discard

	if name == 'A': # Accept
		acc = 1
		for (start, end) in l:
			acc *= (end - start + 1)

		part2 += acc
		continue

	for (lower, index, ope, next_name) in H[name]:
		(st, end) = l[index]

		left = (st, min(ope - 1, end))
		right = (max(ope + 1, st), end)

		if lower == 0:
			if left[0] <= left[1]:
				l1 = l.copy()
				l1[index] = left
				n.append((next_name, l1))

			if right[0] <= right[1]:
				l[index] = (ope, end)
		elif lower == 1:
			if right[0] <= right[1]:
				l1 = l.copy()
				l1[index] = right
				n.append((next_name, l1))

			if left[0] <= left[1]:
				l[index] = (st, ope)
		else:
			n.append((next_name, l))

print("Part2:", part2)