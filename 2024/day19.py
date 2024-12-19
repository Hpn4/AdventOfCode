import sys
from collections import defaultdict

lines = open(sys.argv[1], "r").readlines()

patterns = set()
max_len = 0
for p in lines[0].split(","):
	p = p.strip()
	max_len = max(max_len, len(p))
	patterns.add(p)

def solve(SEEN, c, s, path, paths):
	if s == c:
		if tuple(path) in paths:
			return 0
		paths.add(tuple(path))
		return 1

	if c in SEEN:
		return SEEN[c]

	good = 0
	for i in range(1, max_len + 1):
		p = s[len(c):len(c) + i]
		if p in patterns:
			good += solve(SEEN, c + p, s, path + [p], paths)

	SEEN[c] += good

	return good			

acc = 0
acc2 = 0
for line in lines[2:]:
	res = solve(defaultdict(int), "", line.strip(), [], set())
	if res:
		acc += 1
		acc2 += res

print("Part1:", acc)
print("Part2:", acc2)