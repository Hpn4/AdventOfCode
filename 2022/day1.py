
f = open("input.txt", "r")

lines = f.readlines()

maxs = []
acc = 0
for line in lines:
	line = line.strip()
	if len(line) == 0:
		maxs.append(acc)
		acc = 0
	else:
		acc += int(line)

maxs.sort()
print(maxs[-1] + maxs[-2] + maxs[-3])