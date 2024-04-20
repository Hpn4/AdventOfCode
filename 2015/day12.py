import sys
import json
from collections import deque

lines = open(sys.argv[1], "r").read()
doc = json.loads(lines)

def sum_int(doc, part1):
	q = deque()
	q.append(doc)

	acc = 0
	while q:
		parent = q.popleft()

		if type(parent) == dict:
			red = False
			for k, v in parent.items():
				if v == "red":
					red = True

			if not red or part1:
				for k, v in parent.items():
					q.append(v)
		elif type(parent) == list:
			for el in parent:
				q.append(el)
		elif type(parent) == int:
			acc += parent

	return acc

print("Part1:", sum_int(doc, True))
print("Part2:", sum_int(doc, False))