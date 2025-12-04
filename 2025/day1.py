
lines = open('input1.txt').readlines()

def solve(part1=True):
	count = 50
	acc = 0
	for line in lines:
		line = line.strip()
		if len(line) == 0:
			continue

		r = line[0]
		num = int(line[1:])

		for _ in range(num):
			if r == 'L':
				count -= 1
			else:
				count += 1

			if count < 0:
				count += 100

			if count >= 100:
				count -= 100

			if not part1 and count == 0:
				acc += 1

		if part1 and count == 0:
			acc += 1

	return acc

print("Part1:", solve())
print("Part2:", solve(False))