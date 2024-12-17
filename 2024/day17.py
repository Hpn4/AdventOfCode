import sys

lines = open(sys.argv[1], "r").read()
register, instr = lines.split("\n\n")

reg = [int(x.split(": ")[1].strip()) for x in register.split("\n")]
instr = list(map(int, instr.split(": ")[1].split(",")))

def getCombo(i, reg):
	if 0<=i<=3: return i

	return reg[i - 4]

def solve(reg, instr):
	i = 0
	out = []
	while i < len(instr):
		ins = instr[i]
		op = instr[i + 1]

		if ins == 0:
			reg[0] = reg[0] // 2**getCombo(op, reg)
		elif ins == 1:
			reg[1] = reg[1] ^ op
		elif ins == 2:
			reg[1] = getCombo(op, reg) % 8
		elif ins == 3:
			if reg[0] != 0:
				i = op
				continue
		elif ins == 4:
			reg[1] = reg[1] ^ reg[2]
		elif ins == 5:
			out.append(getCombo(op, reg) % 8)
		elif ins == 6:
			reg[1] = reg[0] // 2**getCombo(op, reg)
		elif ins == 7:
			reg[2] = reg[0] // 2**getCombo(op, reg)

		i += 2

	return out

def p2():
	todo = [(len(instr)-1, 0)]
	for pos, val in todo:
		for a in range(8):
			A = val * 8 + a
			if solve([A, 0, 0], instr) == instr[pos:]:
				todo += [(pos-1, A)]
				if pos == 0:
					return A

print("Part1:", ",".join(map(str, solve(reg, instr))))
print("Part2:", p2())
