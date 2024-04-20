import hashlib

inp = "yzbqklnj"

part1, part2 = 0, 0
i = 0
while True:
	s = inp + str(i)
	res = hashlib.md5(s.encode()).digest()

	if res[0] == 0 and res[1] == 0 and res[2] == 0:
		part2 = i
		break

	if part1 == 0 and res[0] == 0 and res[1] == 0 and res[2] < 8:
		part1 = i

	i += 1

print("Part1:", part1)
print("Part2:", part2)