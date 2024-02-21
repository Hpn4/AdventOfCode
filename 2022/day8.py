import re

a = "te.txt"
aa = "input.txt"
file = open(aa, "r")

# La liste des arbres visibles depuis l'exterieur
coords = []

# On enlève le \n de toutes les lignes du fichier
lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].strip()

def addCoords(x, y):
	if (x, y) not in coords:
		coords.append((x, y))


# On ajoute les arbres tout à gauche et tout à droite
for i in range(0, len(lines)):
	addCoords(0, i) # Arbre à gauche
	addCoords(len(lines[0]) - 1, i) # Arbre à droite

# on ajoute les arbres tout en haut et tout en bas
for i in range(0, len(lines[0]) - 1):
	addCoords(i, 0) # Tout en haut
	addCoords(i, len(lines) - 1) # Tout en bas

# On parcours le tableau suivant l'axe y
# On part de 1 et on s'arrete 1 avant la fin pour éviter de
# tester la première ligne et la dernière
for i in range(1, len(lines) - 1):
	m = lines[i][0]

	for j in range(1, len(lines) - 2):
		if lines[i][j] > m:
			addCoords(j, i)
			m = lines[i][j]

	m = lines[i][-1]
	for j in range(len(lines) - 2, 0, -1):
		if lines[i][j] > m:
			addCoords(j, i)
			m = lines[i][j]

# On parcourt suivant l'axe x
for i in range(1, len(lines[0]) - 1):
	m = lines[0][i]

	for j in range(1, len(lines) - 2):
		v = lines[j][i]
		if v > m:
			addCoords(i, j)
			m = v

	m = lines[-1][i]
	for j in range(len(lines) - 2, 0, -1):
		v = lines[j][i]
		if v > m:
			addCoords(i, j)
			m = v

# Partie 1
print(len(coords))

m = 0
# On parcours que les arbres qui sont visibles depuis l'extérieur pour gagner du temps
for c in coords:
	x = c[0]
	y = c[1]
	mi = lines[y][x]
	counter = 0

	i = x + 1
	right = 0
	while i < len(lines[y]) and lines[y][i] <= mi:
		right += 1
		if lines[y][i] == mi:
			break
		i += 1

	i = x - 1
	left = 0
	while i >= 0 and lines[y][i] <= mi:
		left += 1
		if lines[y][i] == mi:
			break
		i -= 1

	i = y + 1
	bottom = 0
	while i < len(lines) and lines[i][x] <= mi:
		bottom += 1
		if lines[i][x] == mi:
			break
		i += 1

	i = y - 1
	top = 0
	while i >= 0 and lines[i][x] <= mi:
		top += 1
		if lines[i][x] == mi:
			break
		i -= 1

	# On multiplie ce qu'on voit dans les 4 directions
	counter = left * right * top * bottom
	if counter > m:
		m = counter

print(m)