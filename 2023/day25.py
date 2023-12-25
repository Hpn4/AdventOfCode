import sys
from networkx import Graph, minimum_edge_cut, connected_components

lines = open(sys.argv[1], "r").readlines()

G = Graph()
for line in lines:
	name, con = line.strip().split(":")

	for c in con.split():
		G.add_edge(name, c)

for edge in minimum_edge_cut(G):
	G.remove_edge(*edge)

acc = 1
for c in connected_components(G):
	acc *= len(c)

print(acc)