import sys
from collections import defaultdict

# Parsing part
lines = open(sys.argv[1], "r").read()
wires, instrs = lines.split('\n\n')

# Initial values parsing
WIRES = dict()
for wire in wires.split("\n"):
	if wire == "":
		continue

	name, value = wire.strip().split(": ")
	WIRES[name] = int(value)

# Instructions parsing
INSTR = dict()
CACHE = defaultdict(list)
MEM = dict()
for instr in instrs.split("\n"):
	if ">" not in instr:
		continue

	start, res = instr.strip().split(" -> ")

	a, op, b = start.split()
	INSTR[(a,b,res)] = (op)

	MEM[res] = (a, op, b)

	k = (a,b)
	if k not in CACHE:
		k = (b,a)

	CACHE[k].append((op, res))

# Part1 solving
def solve(INSTR, WIRES):
	DONE = set()
	while len(DONE) < len(INSTR):
		for k,op in INSTR.items():
			a,b,res = k

			if a not in WIRES or b not in WIRES:
				continue

			if (a,b,res) in DONE:
				continue
			
			DONE.add((a,b,res))

			a, b = WIRES[a], WIRES[b]

			if op == "AND":
				WIRES[res] = a and b
			elif op == "XOR":
				WIRES[res] = a ^ b
			elif op == "OR":
				WIRES[res] = a or b

	return WIRES

def getValue(WIRES, c):	
	Z = filter(lambda x: x[0] == c, WIRES.keys())
	Z = sorted(Z)
	Z = map(lambda x: str(WIRES[x]), Z)

	s = "".join(Z)

	return int(s[::-1], 2)

WIRES2 = solve(INSTR, WIRES)
print("Part1:", getValue(WIRES2, "z"))

# Part2

# pattern:
# zn = reminder xor (xn xor yn)
# reminder = zn-1 XOR -> AND OR (xn-1 AND xn-1)

## Used to see 
# def build(a):
# 	if a in WIRES:
# 		return a

# 	a, op, b = MEM[a]

# 	return f"({build(a)} {op} {build(b)})"
# for i in range(4):
# 	z = getName("z", i)
# 	print(z, "=", build(z))

def getCache(a, b, op):
	k = (a,b)
	if k not in CACHE:
		k = (b,a)

	if k not in CACHE:
		assert False

	for o,v in CACHE[k]:
		if o == op:
			return v

	assert False

def getCache2(first, op):
	for k,v in CACHE.items():
		a,b = k

		if first != a and first != b:
			continue

		for o,res in v:
			if o == op:
				return res

	assert False

def getName(c, i):
	return c + ("0" if i < 10 else "") + str(i)

swap = []
for i in range(1, 45):
	x = getName("x", i)
	y = getName("y", i)
	z = getName("z", i)
	a, op, b = MEM[z]

	xor = getCache(x, y, "XOR")
	if op != "XOR":
		# print(f"Error for {z} should have a XOR")
		swap.append(z)
		swap.append(getCache2(xor, "XOR"))
		continue
	if a != xor and b != xor:
		# print(f"Error for {z} should XOR with {xor}")
		swap.append(xor)

		if getCache(x, y, "AND") == a:
			swap.append(a)
		else:
			swap.append(b)

swap.sort()
print("Part2:", ",".join(swap))