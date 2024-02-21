import re

class Node:

	def __init__(self, name, flow, children):
		self.name = name
		self.children = children
		self.weights = [1 for _ in range(len(children))]
		self.flow = flow



g = {}

# Partie lecture + parsing du fichier
a = "te.txt"
aa = "input.txt"

lines = []
with open(a) as f:
	for line in f.readlines():
		line = line.strip()

		# Le nombre flow
		nmbs = [int(x) for x in re.findall(r'\d+', line)]

		# Les valves. La première est le nom de la valve et les autres, les fils
		valves = re.findall(r'[A-Z][A-Z]', line)

		node = Node(valves[0], nmbs[0], valves[1:])

		g[valves[0]] = node


def simplify(g, start, visited):
	children = g[start].children
	weights = g[start].weights

	i = 0
	visited.append(start)
	while i < len(children):
		# On récupère le ième fils
		n = g[children[i]]

		if n.name not in visited:
			simplify(g, n.name, visited)

			# Si sa valve est morte, on remonte ses fils
			if n.flow == 0 and children[i] != start:
				j = 0
				while j < len(n.children):
					if n.children[j] == start:
						del n.children[j]
					if n.children[j] != n.name and n.children[j] not in children:
						children.insert(i + 1, n.children[j])
						weights.insert(i + 1, n.weights[j] + 1)
					j += 1

				del children[i]
				del weights[i]

		i += 1


def prune(g):
	visited = {}

	L = ['AA']

	while L:
		a = L.pop()
		visited[a] = 1

		for ch in g[a].children:
			if ch not in visited:
				L.append(ch)

	print(visited)


	for key in g.keys():
		if key not in visited:
			print(key)
			L.append(key)

	for c in key:
		g.pop(c)


for (key, node) in g.items():
	print(key, node.flow, node.children, node.weights)

print("sapce")
simplify(g, 'AA', [])
#prune(g)

for (key, node) in g.items():
	print(key, node.flow, node.children, node.weights)



def bruteForce(g, start, time, p, opened, visited):
	if time == 10:
		return p
	if time > 10:
		return 0

	maxi = p
	for child in g[start].children:
		flow = g[child].flow
		if g[child].flow == 0:
			maxi = max(maxi, bruteForce(g, child, time + 1, p + opened, opened, visited))
		else:
			# On ouvre la valve
			if child not in visited:
				a = bruteForce(g, child, time + 2, p + opened * 2, opened + flow, visited + [child])
				maxi = max(maxi, a)

			# On se déplace juste vers la valve
			b = bruteForce(g, child, time + 1, p + opened, opened, visited)
			maxi = max(maxi, b)

	return maxi

res = bruteForce(g, 'AA', 0, 0, 0, [])
print(res)