import re

lines = open(0, "r").readlines()

acc = 0
acc2 = 0

en = True
for line in lines:
	res = re.findall( r'mul\(([0-9]+),([0-9]+)\)|(do|don\'t)\(\)', line)

	for a,b,c in res:
		if c != '':
			en = c == "do"
		else:
			mul = int(a) * int(b)
			acc += mul
			if en:
				acc2 += mul

print("Part1:", acc)
print("Part2:", acc2)