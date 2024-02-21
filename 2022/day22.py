
lines = open(0).readlines()

# Fonction pour récupérer une liste des mouvements.
# C'est une liste d'entiers pour le nombre de déplacement
# à faire et des lettres pour les sens de rotation
def getMoves(lines):
	move = lines.pop().strip()
	moves = []
	i = 0
	n = 0
	while i < len(move):
		c = move[i]
		if c.isdigit():
			n = n * 10 + ord(c) - ord('0')
		else:
			moves.append(n)
			moves.append(c)
			n = 0

		i += 1

	if n != 0:
		moves.append(n)

	return moves

# On récupère les différentes parties de la junge
# Une partie est considéré comme étant un bloc de ligne ayant la
# même taille et commencant au même endroit.
# Chaque partie sera enregistré sous la forme
# (x, y, size, h) où x,y sont les positions du premier élement du bloc
# au sein de la foret complete.
# size est la taille d'une ligne
# h: correspond au ligne tronqué de leur espaces inutiles
def getParts(lines):
	parts = []
	part = []
	start = min(lines[0].index("."), lines[0].index('#'))
	partSize = len(lines[0].strip())
	y = 0
	for line in lines:
		s = min(line.index(".") if '.' in line else 0, line.index('#') if '#' in line else float('inf'))
		line = line.strip()
		lineSize = len(line)

		if s != start or partSize != lineSize:
			parts.append((start, y, partSize, part))
			y += len(part)
			part = []
			start = s
			partSize = lineSize
		
		part.append(line)

	return parts

# Change l'orientation de notre personnage
def rotate(facing, r):
	add = 1 if r == 'R' else -1
	return (facing + add) % 4

# Retourne l'élement à la casse x,y. On précise aussi sur
# quelle partie du chemin on est
def getAt(x, y, part):
	(xS, yS, _, h) = part

	return h[y - yS][x - xS]

# Déplace notre personnage de un en avant
# Cette fonction renvoie la nouvelle position
# x,y ainsi que la nouvelle part sur laquelle on est
def move(x, y, facing, parts, part):
	(xS, yS, size, h) = part

	if facing == 0:
		x = (x - xS + 1) % size + xS
		return x, y, part

	if facing == 2:
		x = (x - xS - 1) % size + xS
		return x, y, part

	if facing == 3:
		if y - 1 < yS:
			partIndex = parts.index(part) - 1

			# On vérifie qu'on peut pas passer au bloc suivant
			if partIndex >= 0:
				(xS2, yS2, size2, _) = parts[partIndex]
				if xS2 <= x < xS2 + size2:
					return x, y - 1, parts[partIndex]

			# Sinon, il faut warp
			i = len(parts) - 1
			while i >= 0:
				(xS1, yS1, size1, h1) = parts[i]
				if xS1 <= x < xS1 + size1: # On a trouvé où warp
					return x, yS1 + len(h1) - 1, parts[i]

				i -= 1
		return x, y - 1, part

	# Facing == 1
	if y + 1 >= yS + len(h):
		partIndex = parts.index(part) + 1

		# On vérifie qu'on peut pas passer au bloc suivant
		if partIndex < len(parts):
			(xS2, yS2, size2, _) = parts[partIndex]
			if xS2 <= x < xS2 + size2:
				return x, y + 1, parts[partIndex]

		# Si on peut pas, il faut warp
		i = 0
		while i < len(parts):
			(xS1, yS1, size1, _) = parts[i]
			if xS1 <= x < xS1 + size1:
				return x, yS1, parts[i]

			i += 1

	return x, y + 1, part


# On recup les instructions de mouvements
moves = getMoves(lines)

# On récupère les différentes parties de la jungle
parts = getParts(lines)

part = parts[0]
x = part[0] # la position x
y = 0
facing = 0

m = 0
for el in moves:
	if type(el) == int:
		for i in range(el):
			(nX, nY, nP) = move(x, y, facing, parts, part)
			if getAt(nX, nY, nP) == '#':
				break
			else:
				x = nX
				y = nY
				part = nP
	else:
		facing = rotate(facing, el)

	m += 1

part1 = 1000 * (y + 1) + 4 * (x + 1) + facing
print("Partie 1:", part1)

# =============================== #
# ============ Part 2 ===========
# =============================== #

squareSize = 50

# Recupère les faces du cube, pour la partie 2
def getFaces(parts):
	faces = []
	for (x, y, size, h) in parts:
		times = size // squareSize
		hs = [[] for _ in range(times)]
		for line in h:
			for i in range(times):
				l = line[i * squareSize:(i + 1) * squareSize]
				hs[i].append(l)

		for i in range(times):
			faces.append((x + i * squareSize, y, squareSize, hs[i]))

	return faces

faces = getFaces(parts) # On recup les faces

# Toutes les possibilités de mouvements sur les autres faces
# facing: (newFace, newFacing, newX=f(x,y), newY=f(x,y))
face0 = {
	0: (1, 0, lambda x, y: x + 1, lambda x, y: y),
	1: (2, 1, lambda x, y: x, lambda x, y: y + 1),
	2: (3, 0, lambda x, y: faces[3][0], lambda x, y: faces[3][1] + squareSize - 1 - y % squareSize),
	3: (5, 0, lambda x, y: faces[5][0], lambda x, y: faces[5][1] + x % squareSize)
}

face1 = {
	0: (4, 2, lambda x, y: faces[4][0] + squareSize - 1, lambda x, y: faces[4][1] + squareSize - 1 - y % squareSize),
	1: (2, 2, lambda x, y: faces[2][0] + squareSize - 1, lambda x, y: faces[2][1] + x % squareSize),
	2: (0, 2, lambda x, y: x - 1, lambda x, y: y),
	3: (5, 3, lambda x, y: faces[5][0] + x % squareSize, lambda x, y: faces[5][1] + squareSize - 1)
}

face2 = {
	0: (1, 3, lambda x, y: faces[1][0] + y % squareSize, lambda x, y: faces[1][1] + squareSize - 1),
	1: (4, 1, lambda x, y: x, lambda x, y: y + 1),
	2: (3, 1, lambda x, y: faces[3][0] + y % squareSize, lambda x, y: faces[3][1]),
	3: (0, 3, lambda x, y: x, lambda x, y: y - 1)
}

face3 = {
	0: (4, 0, lambda x, y: x + 1, lambda x, y: y),
	1: (5, 1, lambda x, y: x, lambda x, y: y + 1),
	2: (0, 0, lambda x, y: faces[0][0], lambda x, y: faces[0][1] + squareSize - 1 - y % squareSize),
	3: (2, 0, lambda x, y: faces[2][0], lambda x, y: faces[2][1] + x % squareSize)
}

face4 = {
	0: (1, 2, lambda x, y: faces[1][0] + squareSize - 1, lambda x, y: faces[1][1] + squareSize - 1 - y % squareSize),
	1: (5, 2, lambda x, y: faces[5][0] + squareSize - 1, lambda x, y: faces[5][1] + x % squareSize),
	2: (3, 2, lambda x, y: x - 1, lambda x, y: y),
	3: (2, 3, lambda x, y: x, lambda x, y: y - 1)
}

face5 = {
	0: (4, 3, lambda x, y: faces[4][0] + y % squareSize, lambda x, y: faces[4][1] + squareSize - 1),
	1: (1, 1, lambda x, y: faces[1][0] + x % squareSize, lambda x, y: faces[1][1]),
	2: (0, 1, lambda x, y: faces[0][0] + y % squareSize, lambda x, y: faces[0][1]),
	3: (3, 3, lambda x, y: x, lambda x, y: y - 1)
}

cubeMoves = [face0, face1, face2, face3, face4, face5]

def getNewFace(x, y, facing, faces, face):
	index = faces.index(face)

	(nFace, nFacing, fX, fY) = cubeMoves[index][facing]

	return fX(x, y), fY(x, y), faces[nFace], nFacing

movesC = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def moveCube(x, y, facing, faces, face):
	(xS, yS, _, _) = face

	dx, dy = movesC[facing]
	dx += x
	dy += y

	# Out of bound
	if dx >= xS + squareSize or dx < xS or dy >= yS + squareSize or dy < yS:
		return getNewFace(x, y, facing, faces, face)

	return dx, dy, face, facing

# Movement for part 2:
face = faces[0]
x = face[0] # la position x
y = face[1]
facing = 0

m = 0
for el in moves:
	if type(el) == int:
		for i in range(el):
			(nX, nY, nFace, nFacing) = moveCube(x, y, facing, faces, face)
			if getAt(nX, nY, nFace) == '#':
				break
			else: # On met à jour toutes les valeurs
				x = nX
				y = nY
				face = nFace
				facing = nFacing
	else:
		facing = rotate(facing, el)

	m += 1

part1 = 1000 * (y + 1) + 4 * (x + 1) + facing
print("Partie 2:", part1)