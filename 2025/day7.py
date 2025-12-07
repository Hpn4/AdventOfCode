from collections import defaultdict

lines = open("input7.txt").readlines()

grid = [[c for c in line.strip()] for line in lines]

H, W = len(grid), len(grid[0])
x, y = 0, 0
for xx in range(W):
	if grid[0][xx] == "S":
		x = xx

def move_beam(datas, grid, beams):
	acc = 0
	while True:
		bb = set()
		for x, y in beams:
			yy = y + 1

			if yy >= H:
				return acc, datas

			if grid[yy][x] == '^':
				datas[(x - 1, yy)] += datas[(x, y)]
				datas[(x + 1, yy)] += datas[(x, y)]
				acc += 1
				bb.add((x - 1, yy))
				bb.add((x + 1, yy))
			else:
				datas[(x, yy)] += datas[(x, y)]
				bb.add((x, yy))

		beams = bb

	return beams

beams = {(x, y)}
datas = defaultdict(int)
datas[(x, y)] = 1
acc, datas = move_beam(datas, grid, beams)

acc2 = 0
for x in range(W):
	acc2 += datas[(x, H - 1)]

print("Part1:", acc)
print("Part2:", acc2)
