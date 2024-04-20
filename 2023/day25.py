import sys
import networkx as nx

lines = open(sys.argv[1], "r").readlines()

G = nx.Graph()
for line in lines:
	name, con = line.strip().split(":")

	for c in con.split():
		G.add_edge(name, c)

for edge in nx.minimum_edge_cut(G):
	G.remove_edge(*edge)

acc = 1
for c in nx.connected_components(G):
	acc *= len(c)

print(acc)