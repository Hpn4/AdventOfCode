from collections import defaultdict

line = open(0, "r").readlines()[0].strip()

l = []
for i in range(len(line)):
	id_ = i // 2 if i % 2 == 0 else -1
	l.append((id_, int(line[i])))

l2 = [x for x in l]

# Integer sum from pos to pos + 2 * scalar id_
def sum2(pos, id_, size):
	return (size * (2 * pos + size - 1) * id_) // 2

acc = 0
pos = 0
last = len(line) - 1
i = 0
while i < len(line):
	id_, size = l[i]

	if last <= i:
		break

	# Free block
	if id_ == -1:
		id2, size2 = l[last]
		if id2 == -1:
			last -= 1
			continue

		de = min(size, size2)

		acc += sum2(pos, id2, de)

		pos += de
		l[last] = (id2, size2 - de)
		l[i] = (id_, size - de)

		if size2 == de: # File completly moved
			last -= 2

		if size == de: # Empty block move on
			i += 1
	else:
		acc += sum2(pos, id_, size)
		pos += size
		i += 1

print(acc)
acc2 = 0
pos = 0
i = 0
last = len(l2) - 1
while i < len(l2):
	id_, size = l2[i]

	if id_ == -1:
		x = i
		empty = False
		for j in range(last, x, -2):
			id2, size2 = l2[j]
			if id2 == -1 or size2 == 0 or size < size2:
				continue

			acc2 += sum2(pos, id2, size2)

			pos += size2
			size -= size2 # Decrease free size

			# Mark block of moved file as free
			l2[j] = (-1, size2)
			# Update size of the current free block
			l2[i] = (id_, size)

			if j == last:
				last -= 2

			if size == 0:
				empty = True
				break

		pos += size
		i += not empty
	else:
		acc2 += sum2(pos, id_, size)
		pos += size
		i += 1

print("Part1:", acc)
print("Part2:", acc2)