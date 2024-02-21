
# C'est cette fonction qui va faire la "physique" des déplacements des noeuds
def moveTail(h, t):
	# On calcul la différence entre la tête et la queue suivant
	# l'axe X et l'axe Y
	dX, dY = h[0] - t[0], h[1] - t[1]

	if dX == 0: # Si la différence des X est à 0 cela signifie qu'ils sont sur la même colonne
		# Revient à tester si la queue est des Y plus haut ou bien deux Y plus bas
		if abs(dY) >= 2:
			# Revient à diviser par deux dY
			# l'instruction "a >> n" veut dire "décaler tous les bits de a n fois vers la droite"
			# Les décaler une fois revient à diviser par 2, 2 fois à 4 et ainsi de suite.
			# Il y a egalement l'opérateur inverse << qui comme tu peux t'en douter, va multiplier.
			# << 1 multiplie par 2, << 2 par 4, etc...
			# 
			# On divise par 2 car si
			# dY == 2 => notre tête est une case au dessus, la queue doit donc monter vers le haut
			# dY == -2 => notre tête est en dessous, la queue vas descendre
			t[1] += dY >> 1
	elif dY == 0: # Si ils sont sur le même axe Y = même ligne
		# Même raisonnement qu'au dessus
		if abs(dX) >= 2:
			t[0] += dX >> 1 # Revient à diviser par deux dX
	elif abs(dY) + abs(dX) > 2: # tests pour les diagonales
		# Cette partie là à été optimisé pour avoir le moins de condition et de calcul
		# possible, donc c'est normal que ce soit pas compréhensible
		# Grosso modo ça gère le cas de toutes les diagonales.
		# Pour expliquer pk j'ai fait ces calculs, il faudrait faire un petit
		# dessin et voire qu'en fait ça prend bien en compte tous les cas de figure.
		if abs(dY) == 1:
			t[1] += dY
			t[0] += dX >> 1
		elif abs(dX) == 1:
			t[0] += dX
			t[1] += dY >> 1
		else:
			t[1] += dY >> 1
			t[0] += dX >> 1

a = "te.txt"
aa = "input.txt"
file = open(aa, "r")

# Ici je crée un set python. Comme je te l'avais expliqué, un set équivaut à un ensemble mathématique.
# C'est-à-dire qu'il n'y a pas de notion d'ordre et qu'il ne peut pas y avoir plusieurs fois le même élements.
coords = {(0, 0)}

# Mettre à 2 pour la partie 1, correspond aux nombres de noms de la corde
knots = 10
ropes = [[0, 0] for i in range(knots)] # on crée notre corde

# On pré-enregistre les mouvements que l'on va faire en fonction de la lettre.
# Le format est 'Lettre' : (se déplacer de combien en X, se déplacer de combien en Y)
moveDir = {'D': (0, -1), 'U': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

# On parcours l'entièreté de notre fichier
for line in file.readlines():
	line = line.strip()

	# Petite pythonerie.
	# ça equivaut à faire:
	# parts = line.split(" ")
	# direction = parts[0]
	# toMove = parts[1]
	direction, toMove = line.split()

	# On récupère nos variations en x et en y
	(x, y) = moveDir[direction]

	# On répète toMove fois le mouvement
	for i in range(int(toMove)):
		# On bouge notre tête
		ropes[-1][0] += x
		ropes[-1][1] += y

		# Puis on bouge chaque élement 1 à 1
		for i in range(knots - 1, 0, -1):
			moveTail(ropes[i], ropes[i - 1])

		# Finalement on ajoute notre queue
		coords.add((ropes[0][0], ropes[0][1]))

# Comme on travaille avec un set, il n'y a pas de doublons alors on a directement
# le nombre de positions différente en obtenant la taille
print(len(coords))