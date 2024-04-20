import sys

lines = open(sys.argv[1], "r").readlines()
lines = [line.strip() for line in lines]

code, real = 0, 0
for line in lines:
	code += len(line)
	i = 1
	while i < len(line) - 1:
		if line[i] == '\\':
			i += 1
			if line[i] == 'x':
				i += 2

		real += 1
		i += 1

esc = 0
for line in lines:
	for c in line:
		if c == '"' or c == '\\':
			esc += 2
		else:
			esc += 1

	esc += 2

print("Part1:", code - real)
print("Part2:", esc - code)