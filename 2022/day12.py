import re
from queue import Queue

a = "te.txt"
aa = "input.txt"
file = open(aa, "r")

# On enlève tous les caractères de fin de ligne
lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].strip()
file.close()

# Quelques variables utilitaires
# startIndex retient la position du S
# endIndex celle du E
startIndex = 0
endIndex = 0
width = len(lines[0])
height = len(lines)

# Fonction utilitaire, ajoute un enfant au noeud node
# ssi il y a une différence de 1 entre les niveaux de c (current)
# et toGo
def addWeightedEdge(c, toGo, node, pos):
	if toGo == 'E':
		toGo = 'z'

	if ord(toGo) <= ord(c) + 1:
		node.append(pos)

# le graph
g = []

# I parse the entiere file and create a weighted graph
coords = []
for y in range(height):

	for x in range(width):
		children = []
		current = lines[y][x]
		currentPos = y * width + x

		# On enregistre la position de départ et d'arrivé
		if current == 'S':
			startIndex = currentPos
			current = 'a'
		if current == 'E':
			endIndex = currentPos
			current = 'z'

		# Si c'est un a, on l'enregistre dans la liste des points
		# de départ
		if current == 'a':
			coords.append(currentPos)

		# On regarde si on peut aller à gauche
		# Si oui, on récupère l'élement à gauche, on calcul son index et on
		# tente de l'ajouter en fils
		if x - 1 >= 0:
			el = lines[y][x - 1]
			pos = y * width + x - 1

			addWeightedEdge(current, el, children, pos)

		# On regarde si on peut aller à droite, même raisonnement
		if x + 1 < width:
			el = lines[y][x + 1]
			pos = y * width + x + 1

			addWeightedEdge(current, el, children, pos)

		# En haut
		if y - 1 >= 0:
			el = lines[y - 1][x]
			pos = (y - 1) * width + x

			addWeightedEdge(current, el, children, pos)

		# En bas
		if y + 1 < height:
			el = lines[y + 1][x]
			pos = (y + 1) * width + x

			addWeightedEdge(current, el, children, pos)

		# Finalement on ajoute les déplacements possible dans notre graph
		g.append(children)

# On va parcourir notre graph en largeur (grâce à une queue)
# C'est le même raisonnement qu'avec les arbres, les graphes peuvent
# être parcourue soit en profondeur, soit en largeur.
# Le parcour largeur permet d'avancer niveau par niveau.
# Visuellement cela va faire comme des cercles autour de notre point de départ.
# On regarde à une distance de 1 de notre point de départ ce qu'il y a,
# puis à une distance de 2, de 3... etc..
# Ici je le fait jusqu'a tomber sur le noeud de fin
def shortest(g, i, end, M):
	q = Queue()
	q.put(i)
	M[i] = 0

	while not q.empty():
		v = q.get()

		if v == end:
			return M[v]

		for child in g[v]:
			if M[child] == -1:
				q.put(child)
				M[child] = M[v] + 1

	return float('inf')


# Partie 1:
path = [-1 for i in range(len(g))]
mini = shortest(g, startIndex, endIndex, path)
print("Partie 1:", mini)

# Partie 2:
# Cette partie est assez pas opti mais bon j'avais la flemme
# de faire plus propre, en soit j'ai testé d'autres trucs et il y a pas
# vraiment de meilleure méthode
for c in coords:
	path = [-1 for i in range(len(g))]
	d = shortest(g, c, endIndex, path)

	if d < mini:
		mini = d

print("minimal:", mini)