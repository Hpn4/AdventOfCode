
lines = open('input4.txt').readlines()

grid = [[c for c in line.strip()] for line in lines]

W, H = len(grid[0]), len(grid)

def can_access(x, y, grid):
	D = [-1, 0, 1]

	acc = 0
	for dx in D:
		for dy in D:

			if dx == 0 and dy == 0:
				continue

			xx = dx + x
			yy = dy + y

			if xx < 0 or yy < 0 or xx >= W or yy >= H:
				continue

			if grid[yy][xx] == "@":
				acc += 1

	return acc < 4

def get_access(grid):
	points = []
	for x in range(W):
		for y in range(H):
			if grid[y][x] == '@' and can_access(x, y, grid):
				points.append((x, y))

	return points

# Part 1
first = get_access(grid)
print("Part1:", len(first))

# Part 2
acc = len(first)
while len(first) > 0:
	for x,y in first:
		grid[y][x] = '.'

	first = get_access(grid)
	acc += len(first)

print("Part2:", acc)
