import sys
import networkx as nx

lines = open(sys.argv[1], "r").readlines()

G = nx.Graph()
for line in lines:
	town, dist = line.split(" = ")
	src, _, dst = town.split()

	G.add_edge(src, dst, weight=int(dist))

def seaman(p1, G, start, seen, d):
	if len(seen) == len(G):
		return d

	seen.add(start)
	m = 1e10 if p1 else 0
	for node, weight in G[start].items():
		if node in seen:
			continue

		cpy = seen.copy()
		cpy.add(node)

		se = seaman(p1, G, node, cpy, d + weight['weight'])
		if p1:
			m = min(m, se)
		else:
			m = max(m, se)

	return m

part1 = 1e10
for node in G:
	part1 = min(part1, seaman(True, G, node, set(), 0))

part2 = 0
for node in G:
	part2 = max(part2, seaman(False, G, node, set(), 0))

print("Part1:", part1)
print("Part2:", part2)