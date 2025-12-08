import numpy as np

lines = open("input8.txt").readlines()

# Parsing
boxes = [[int(a) for a in line.strip().split(",")] for line in lines]
circuits = {}

# Distance matrix sorted
boxes = np.array(boxes)

D = np.sqrt(((boxes[:, None, :] - boxes[None, :, :]) ** 2).sum(axis=2))
np.fill_diagonal(D, np.inf)

idx = np.argsort(D.copy(), axis=None)
i, j = np.unravel_index(idx, D.shape)

def find_circ(box):
	b = tuple(box.tolist())
	for k,v in circuits.items():

		if b in v:
			return k

	return -1

circ = 0
k = 0
while True:
	box_a = boxes[i[2 * k]]
	box_b = boxes[j[2 * k]]
	k += 1
	circ_a, circ_b = find_circ(box_a), find_circ(box_b)

	if circ_a == -1 and circ_b == -1:
		circuits[circ] = { tuple(box_a.tolist()), tuple(box_b.tolist()) }
		circ += 1
		continue

	if circ_a == circ_b: # Same circuits
		continue

	# Merge circuits:
	if circ_a == -1:
		circuits[circ] = { tuple(box_a.tolist()) }.union(circuits.pop(circ_b))
		circ += 1
	elif circ_b == -1:
		circuits[circ] = { tuple(box_b.tolist()) }.union(circuits.pop(circ_a))
		circ += 1
	else:
		first = circuits.pop(circ_a)
		circuits[circ_b].update(first)

	val = [len(x) for x in circuits.values()]

	if k == 1000:
		val = sorted(val)
		print("Part1:", val[-1] * val[-2] * val[-3])

	if max(val) == len(boxes):
		print("Part2:", box_a[0] * box_b[0])
		break