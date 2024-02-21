import re

# Partie lecture de fichier
a = "te.txt"
aa = "input.txt"

partie2 = False

lines = []
with open(aa) as f:
	for line in f.readlines():
		lines.append(line.strip())

minX, maxX = 1000, 0
minY, maxY = 1000, 0

paths = []
for line in lines:
	nmbs = [(int(x), int(y)) for (x, y) in re.findall(r'(\d+),(\d+)', line)]
	
	for (x, y) in nmbs:
		minX = min(minX, x)
		maxX = max(maxX, x)

		minY = min(minY, y)
		maxY = max(maxY, y)

	paths.append(nmbs)


# Pour la partie 2, on augmente les bornes:
if partie2:
	minX = 0
	maxY += 2
	maxX += maxY

# Les dimensions de la cave
width = maxX - minX + 1
height = maxY + 1

# On construit un histogramme
h = [[" " for _ in range(width)] for _ in range(height)]

def draw(pointA, pointB):
	startX = pointA[0] - minX
	startY = pointA[1]
	endX = pointB[0] - minX
	endY = pointB[1]

	if(startY == endY):
		for x in range(min(startX, endX), max(startX, endX) + 1):
			h[startY][x] = "#"
	else:
		for y in range(min(startY, endY), max(startY, endY) + 1):
			h[y][startX] = "#"

for path in paths:
	i = 0
	while i < len(path) - 1:
		draw(path[i], path[i + 1])
		i += 1

# Pour la partie 2:
# La dernière ligne tout en bas
if partie2:
	draw((minX, height - 1), (maxX, height - 1))

# Partie du sable
counter = 0
canAdd = True
while(canAdd):
	sandX = 500 - minX
	sandY = 0

	move = True
	while(sandX >= 0 and sandX < width and sandY + 1 < height and move):
		if h[sandY + 1][sandX] == " ":
			sandY += 1
		elif h[sandY + 1][sandX - 1] == " ":
			sandY += 1
			sandX -= 1
		elif h[sandY + 1][sandX + 1] == " ":
			sandY += 1
			sandX += 1
		else:
			move = False

	if not move:
		# On a pas bouger de l'emetteur, on peut plus ajouter de sable, cette condition est
		# pour la partie 2
		if sandX == 500 - minX and sandY == 0:
			canAdd = False
			counter += 1
		else:
			counter += 1
			h[sandY][sandX] = "o"
	else:
		canAdd = False

print(counter)