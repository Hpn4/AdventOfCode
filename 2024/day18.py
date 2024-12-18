import heapq
import sys
from helper import DIRS

lines = open(sys.argv[1], "r").readlines()

size = 70

# Load the n first bytes
def load(n):
	BYTE = set()
	for i in range(n):
		a,b = map(int, lines[i].strip().split(","))

		BYTE.add((a,b))

	return BYTE

def solve(n):
	BYTE = load(n)
	Q = []
	heapq.heappush(Q, (0,0,0))
	SEEN = set()
	while Q:
		d, x, y = heapq.heappop(Q)

		if (x,y) in SEEN or (x,y) in BYTE:
			continue

		SEEN.add((x,y))

		if x == size and y == size:
			return d

		for (dx,dy) in DIRS:
			xx,yy = x + dx, y + dy

			if 0<=xx<=size and 0<=yy<=size and (xx,yy) not in BYTE and (xx,yy) not in SEEN:
				heapq.heappush(Q, (d+1, xx, yy))

	return None

# Binary search for part 2
s = 2025
e = len(lines)
while s + 1 < e:
	i = (e - s) // 2 + s

	if solve(i) is None:
		e = i
	else:
		s = i

print("Part1:", solve(1024))
print("Part2:", lines[s].strip())