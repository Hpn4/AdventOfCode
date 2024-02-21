import re

file = open("input.txt", "r")

# La variable x qui sera incrementer via les insctructions addx
x = 1

# Pour la partie 1, la première variable retient le cycle auquel ont est.
# La deuxième est un tableau des cycles auquel il faudra faire l'opération acc += x * cycle
# Et la dernière est notre accumulateur des valeur de x multiplié par le cycle
cycle = 0
cycles = [20, 60, 100, 140, 180, 220]
acc = 0

# Pour la partie 2
# Les dimensions de "l'écran"
screenWidth, screenHeight = 40, 6
screen = ["" for _ in range(screenHeight)] # L'écran en lui même est une liste de string
xPos, yPos = 0, 0 # L'emplacement du pixel que l'on est en train de dessiner

for line in file.readlines():
	line = line.strip()

	# On récupère les nombres de la lignes.
	# si len(nmbs) == 0 => pas de nombre => noop instruction
	# si len(nmbs) == 1 => nombre dans la ligne => addx instruction
	nmbs = [int(s) for s in re.findall(r'-?\d+', line)]

	# Si c'est une instruction addx, on répète deux fois le code suivant, sinon une fois
	loop = 2 if len(nmbs) == 1 else 1
	for _ in range(loop):
		# Si on est dans l'emplacement 
		if x - 1 <= xPos <= x + 1:
			screen[yPos] += "#"
		else:
			screen[yPos] += "."

		# Propre à la partie 1, on augmente le cycle et on augmente
		# notre accumulateur si c'est un cycle important
		cycle += 1
		if cycle in cycles:
			acc += x * cycle

		# On passe au pixel suivant et si on est à la fin, on va à la ligne
		xPos += 1
		if xPos >= screenWidth:
			xPos = 0
			yPos += 1

	# On incremente la variable X ssi il y avait un nombre dans la ligne
	if len(nmbs) > 0:
		x += nmbs[0]

# Partie 1
print(acc)

# Partie 2
for i in screen:
	print(i)