lines = open(0, "r").readlines()
grid = [[int(x) for x in line.strip()] for line in lines]

P = set()
def trail(cache, x, y, grid):
	acc = 0
	key = (x, y)
	he = grid[y][x]

	if key in cache:
		return cache[key]

	if he == 9:
		P.add((x,y))
		return 1

	width, height = len(grid[0]), len(grid)

	right = x + 1
	left = x - 1
	top = y - 1
	bot = y + 1

	if left >= 0 and grid[y][left] == he + 1:
		acc += trail(cache, left, y, grid)

	if right < width and grid[y][right] == he + 1:
		acc += trail(cache, right, y, grid)

	if top >= 0 and grid[top][x] == he + 1:
		acc += trail(cache, x, top, grid)

	if bot < height and grid[bot][x] == he + 1:
		acc += trail(cache, x, bot, grid)

	cache[key] = acc

	return acc

acc = 0
acc2 = 0
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == 0:
			P = set()

			acc2 += trail(dict(), x, y, grid)
			acc += len(P)

print("Part1:", acc)
print("Part2:", acc2)