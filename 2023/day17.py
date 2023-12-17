import sys
import heapq

lines = open(sys.argv[1], "r").readlines()
lines = [[int(c) for c in line.strip()] for line in lines]

w = len(lines[0])
h = len(lines)

def solve(part1):
	Q = [(0, 0, 0, -1, -1)]
	D = {}
	ans = 10**9

	while Q:
		d, x, y, o, di = heapq.heappop(Q)
		key = (x, y, o, di)

		if key in D:
			continue

		D[key] = d
		for i,(accX, accY) in enumerate([[-1,0], [0, -1], [1,0], [0, 1]]):
			if (o + 2) % 4 == i: # Go in inverse dir
				continue

			x2 = x + accX
			y2 = y + accY

			new_indir = (1 if i != o else di + 1)

			if part1:
				valid = new_indir <= 3
			else:
				valid = new_indir <= 10 and (i == o or di >= 4 or di == -1)

			if 0 <= x2 < w and 0 <= y2 < h and valid:
				cost = d + lines[y2][x2]
				if x == w - 1 and y == h - 1:
					ans = min(ans, d)
				else:
					heapq.heappush(Q, (cost, x2, y2, i, new_indir))

	return ans

print("Part1:", solve(True))
print("Part2:", solve(False))