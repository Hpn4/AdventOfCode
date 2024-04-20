import sys
import re

lines = open(sys.argv[1], "r").readlines()

"""
turn off 235,899 through 818,932
turn on 445,611 through 532,705
toggle 629,387 through 814,577
"""

s = range(1000)
light1 = [[False for _ in s] for _ in s]
light2 = [[0 for _ in s] for _ in s]

for line in lines:
	t = 2
	if "on" in line:
		t = 1
	elif "off" in line:
		t = -1

	sx,sy,ex,ey = [int(x) for x in re.findall("\d+", line)]

	for x in range(sx, ex + 1):
		for y in range(sy, ey + 1):
			light2[y][x] = max(0, t + light2[y][x])

			if t == 2:
				light1[y][x] ^= True
			elif t == 1:
				light1[y][x] = True
			else:
				light1[y][x] = False

part1, part2 = 0, 0
for y in s:
	part1 += sum(light1[y])
	part2 += sum(light2[y])

print("Part1:", part1)
print("Part2:", part2)

# 14747699	