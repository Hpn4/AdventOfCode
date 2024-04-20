import sys
import networkx as nx

lines = open(sys.argv[1], "r").readlines()

G = nx.DiGraph()
for line in lines:
	line = line.strip()
	words = line.split()

	src = words[0]
	dst = words[-1][:-1]

	dist = int(words[3])
	if "lose" in line:
		dist = -dist

	if G.has_edge(src, dst):
		G[src][dst]['weight'] += dist
		G[dst][src]['weight'] += dist
	else:
		G.add_edge(src, dst, weight=dist)
		G.add_edge(dst, src, weight=dist)

def seaman(G, start, seen, d):
	m = 0
	for node, weight in G[start].items():
		if node == seen[0] and len(set(seen)) == len(G):
			return d + weight['weight']

		if node in seen:
			continue

		se = seaman(G, node, seen + [node], d + weight['weight'])
		m = max(m, se)

	return m

part1 = 0
for node in G:
	part1 = max(part1, seaman(G, node, [node], 0))

# Part2
G.add_node('Me')
for node in G:
	if node != 'Me':
		G.add_edge(node, 'Me', weight=0)
		G.add_edge('Me', node, weight=0)

part2 = 0
for node in G:
	part2 = max(part2, seaman(G, node, [node], 0))

print("Part1:", part1)
print("Part2:", part2)