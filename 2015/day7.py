import sys

lines = open(sys.argv[1], "r").readlines()

var = {}
def varOrNum(s):
	if s in var:
		return var[s]

	if s[0].isdigit():
		return int(s)

	return None

bset = 0
for j in range(2):
	done = set()
	if j == 1:
		done.add(bset)
	for _ in lines:
		for i,line in enumerate(lines):
			if i in done:
				continue

			left, right = line.strip().split(" -> ")
			if right == 'b':
				bset = i

			if "NOT" in left:
				v = varOrNum(left[4:])
				if v is None:
					continue
				var[right] = 65535 - v
				done.add(i)
			elif " " in left:
				l, op, r = left.split()
				l = varOrNum(l)
				r = varOrNum(r)
				if l is None or r is None:
					continue

				if op == "AND":
					var[right] = l & r
				elif op == "OR":
					var[right] = l | r
				elif op == "LSHIFT":
					var[right] = l << r
				elif op == "RSHIFT":
					var[right] = l >> r
				else:
					assert False

				done.add(i)
			else:
				v = varOrNum(left)
				if v is None:
					continue
				var[right] = v

				done.add(i)

	acc = var['a']
	var.clear()
	var['b'] = acc
	print(f"Part{j + 1}:", acc)
