import sys

lines = open(sys.argv[1], "r").readlines()

patterns = set()
max_len = 0
for p in lines[0].split(","):
	p = p.strip()
	max_len = max(max_len, len(p))
	patterns.add(p)

SEEN = {}
def solve(s):
	if not s:
		return 1

	if s in SEEN:
		return SEEN[s]

	good = 0
	for i in range(1, min(max_len, len(s)) + 1):
		p = s[:i]
		if p in patterns:
			good += solve(s[i:])

	SEEN[s] = good

	return good			

acc = 0
acc2 = 0
for line in lines[2:]:
	res = solve(line.strip())
	if res:
		acc += 1
		acc2 += res

print("Part1:", acc)
print("Part2:", acc2)