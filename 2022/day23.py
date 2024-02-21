import re
from collections import deque

# On lit les fichiers
lines = [x.strip() for x in open(0).readlines()]

# Cette fonction renvoi un ensemble de la position des elfs.
def getElvesSet(lines):
	elves = set()
	x = 0
	y = 0
	for line in lines:
		for c in line:
			if c == "#":
				elves.add((x, y))

			x += 1

		x = 0
		y += 1

	return elves

# Retourne le nombre de tile vide dans le rectangle le plus petit qui contient
# tous les elfes
def getNumberOfETiles(elves):
	xMin = float('inf')
	xMax = -float('inf')

	yMin = float('inf')
	yMax = -float('inf')

	for (x, y) in elves:
		xMin = min(x, xMin)
		xMax = max(x, xMax)

		yMin = min(y, yMin)
		yMax = max(y, yMax)

	width = xMax - xMin + 1
	height = yMax - yMin + 1

	# Le nombre de tile vide est l'air du rectangle moins
	# le nombre d'elfes
	return width * height - len(elves)

# Ajoute le mouvement de (x, y) -> (newX, newY)
# Cette fonction va gérer les conflits et ce genre de chose
def addMove(x, y, newX, newY, proposed, end, conflict):
	endPos = (newX, newY)

	# C'est déjà une position à conflit
	if endPos in conflict:
		pass

	# C'est une position qui vient de créer un conflit
	elif endPos in end:
		conflict.add(endPos)
	# Sinon, on l'ajoute normalement
	else:
		end.add(endPos)
		proposed.append((x, y, newX, newY))

# elve: L'elf qu'on veut déplacer
# elves: l'ensemble de tous les elfs
# proposed: une liste des déplacements qui on été proposés. De la forme (x, y, newX, newY)
# end: un ensemble des positions de fin proposées (newX, newY)
# conflict: un ensemble des positions qui sont déjà dans end (newX, newY) 
# directions: une liste pour l'ordre des directions
def tryToMove(elve, elves, proposed, end, conflict, directions):
	(x, y) = elve

	# En premier on vérifie qu'il a personne au tour de lui
	"""
	hasElves = (x - 1, y - 1) in elves
	hasElves = hasElves or (x, y - 1) in elves
	hasElves = hasElves or (x + 1, y - 1) in elves

	hasElves = hasElves or (x - 1, y) in elves
	hasElves = hasElves or (x + 1, y) in elves

	hasElves = hasElves or (x - 1, y + 1) in elves
	hasElves = hasElves or (x, y + 1) in elves
	hasElves = hasElves or (x + 1, y + 1) in elves
	"""
	hasElves = False
	for dx in range(-1, 2, 1):
		for dy in range(-1, 2, 1):
			if not (dx == 0 and dy == 0) and hasElves == False:
				hasElves = hasElves or (x + dx, y + dy) in elves

	# Si il y a des elfes ont va tenter de bouger
	if hasElves:
		for d in directions:
			if d == 'N' or d == 'S':
				dy = y + (1 if d == 'S' else -1)
				if (x - 1, dy) not in elves and (x, dy) not in elves and (x + 1, dy) not in elves:
					addMove(x, y, x, dy, proposed, end, conflict)
					return

			else:
				dx = x + (1 if d == 'E' else -1)
				if (dx, y - 1) not in elves and (dx, y) not in elves and (dx, y + 1) not in elves:
					addMove(x, y, dx, y, proposed, end, conflict)
					return

def printHist(elves):
	h = [['.' for _ in range(15)] for _ in range(15)]

	for (x, y) in elves:
		h[y][x] = "#"

	for line in h:
		buf = ""
		for c in line:
			buf += c
		print(buf)

# On recup les elfs
elves = getElvesSet(lines)

directions = ['N', 'S', 'W', 'E']

r = 0
p1 = 0
while(True):
	# On réinitialise toutes les variables
	proposed = []
	conflict = set()
	end = set()

	# On déplace tous les elfes
	for elve in elves:
		tryToMove(elve, elves, proposed, end, conflict, directions)

	# Si aucun peut bouger, on arrête
	if len(proposed) == 0 or (len(proposed) - len(conflict) == 0):
		break

	# On regarde tous les mouvements proposés
	for (x, y, newX, newY) in proposed:
		if (newX, newY) not in conflict:
			elves.remove((x, y))
			elves.add((newX, newY))

	# On met à jour les directions
	directions.append(directions.pop(0))
	r += 1

	# Pour la partie 1 on calcul le nombre de tile vide au round 10
	if r == 10:
		p1 = getNumberOfETiles(elves)

print("Partie 1:", p1)
print("Partie 2:", r + 1)