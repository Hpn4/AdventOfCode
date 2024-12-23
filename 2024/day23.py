import sys
from collections import deque, defaultdict
from itertools import permutations, combinations

lines = open(sys.argv[1], "r").readlines()

# Parsing and keep track of nodes starting with 't'
G = defaultdict(set)
T = []
for line in lines:
	a,b = line.strip().split("-")

	G[a].add(b)
	G[b].add(a)
	if a[0] == 't':
		T.append(a)
	if b[0] == "t":
		T.append(b)

def in_set(SET, x):
	for a,b,c in permutations([0, 1, 2]):
		key = (x[a],x[b],x[c])
		if key in SET:
			return True

	return False

def solve1(G, T):
	SET = set()
	for t in T:
		for n,n1 in combinations(G[t], 2):
			if n == t or n1 == t:
				continue
			if n not in G[n1]:
				continue
			key = (t,n,n1)

			if in_set(SET, key):
				continue

			SET.add(key)

	return SET

# Part 2
def BronKerbosch(ALL, R, P, X):
	if len(P) == 0 and len(X) == 0:
		ALL.append(R)
		return

	u = None
	for i in P:
		u = i
		break

	for v in (P - G[u]):
		nei = G[v]
		BronKerbosch(ALL, R | set([v]), P & nei, X & nei)
		P.remove(v)
		X.add(v)

ALL = []
BronKerbosch(ALL, set(), set(G.keys()), set())

larg = max(ALL, key=len)
larg = sorted(larg)

# Result
print("Part1:", len(solve1(G, T)))
print("Part2:", ",".join(larg))