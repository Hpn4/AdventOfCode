from collections import deque

# Partie lecture + parsing du fichier
aa = "input.txt"

# Partie lecture de fichier et parsing
lines = list(map(lambda l: l.strip(), open(aa).readlines()))
gasDirection = [-1 if c == "<" else 1 for c in lines[0]] # -1 gauche, 1 droite

# Chaque forme est un triplet (x, y, t) où (x, y) est les coordoonées du bas de la forme
# Pour le - c'est tout à gauche, pour le | tout en bas, le + en bas de barre du |.
# t représente le type: t=0 => -, t=1 => +, t=2 => _|, t=3 => |, t=4 => o
minus = [[1, 1, 1, 1]]
plus = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
angle = [[1, 1, 1], [0, 0, 1], [0, 0, 1]]
barre = [[1], [1], [1], [1]]
square = [[1, 1], [1, 1]]

shapes = [(e, 7 - len(e[0])) for e in [minus, plus, angle, barre, square]]

# On déssine notre forme dans notre histogramme
def drawShape(xA, yA, tA, S):
	shape = tA[0]
	x, y = xA, yA
	for line in shape:
		for c in line:
			S[-y][x] += c
			x += 1
		x = xA
		y += 1

# Cette fonction renvoi vrai si A collissionne avec au moins une des formes de elements
def collide(A, elements):
	(xA, yA, tA) = A

	for (xB, yB, tB) in elements:
		dY = yA - yB

		# Si il y a trop d'espace, on s'embete par car il y a aucune chance que
		# ça collissionne
		if dY >= 4 or dY < -3:
			continue

		# On construit un histogramme pour dessiner nos formes dessus
		co = [[0 for _ in range(7)] for _ in range(7)]

		# On déssine nos formes en empechant y d'être trop grand
		m = min(yA, yB)
		drawShape(xB, yB - m, tB, co)
		drawShape(xA, yA - m, tA, co)

		for line in co:
			for el in line:
				if el >= 2: # Deux formes se superposent
					return True
	return False

# Petite fonction clamp. Quelle que soit la valeur de x, il sera ramené dans l'intervalle [l, u]
clamp = lambda x, l, u: l if x < l else u if x > u else x

def getTall(total):
	# Index pour le gas et la forme
	gasIndex, t = 0, 0

	# Variable pour les cycles
	befT, befTurn = 0, 0
	endCycle = False
	cycles = []

	# Game variable
	ySpawn = 3
	turn = 0
	elements = deque() # Une queue
	tall = 0
	while turn < total:
		x, y = 2, ySpawn
		shape = shapes[t]
		pad, height = shape[1], len(shape[0])

		endCycle = False

		while not collide((x, y, shape), elements) and y >= 0:
			d = gasDirection[gasIndex]

			gasIndex += 1
			if gasIndex >= len(gasDirection):
				gasIndex = 0
				endCycle = True

			bef = x
			x = clamp(x + d, 0, pad)

			if collide((x, y, shape), elements):
				x = bef

			y -= 1

		# Si on sort de la boucle = collission
		y += 1

		# On ne garde en mémoire que les 25 dernières formes, ça sert à rien de s'encombrer avecles autres.
		# Le nombre 25 est un peu random à vrai dire. (on peut l'augmenter si mauvaise solution)
		elements.append((x, y, shape))
		if len(elements) > 25:
			elements.popleft()

		tall = max(tall, y + height)
		if endCycle:			
			cycles.append((turn - befTurn, tall - befT))

			befTurn = turn
			befT = tall

		ySpawn = tall + 3

		turn += 1

		# On change la forme
		t += 1
		if t > 4:
			t = 0

	return tall, cycles


def getPartie1():
	print("Partie 1:", getTall(2022)[0])

def getPartie2():
	total = 1000000000000
	(_, cycles) = getTall(3700)

	firstCycleTurn = cycles[0][0] + 1
	(cycleTurn, cycleTall) = cycles[1]

	tallOpti = 0
	total -= firstCycleTurn

	redo = int(total / cycleTurn)
	tallOpti = redo * cycleTall
	total -= redo * cycleTurn

	total += firstCycleTurn

	tallOpti += getTall(total)[0]
	print("Partie 2:", tallOpti)

getPartie1()
getPartie2()