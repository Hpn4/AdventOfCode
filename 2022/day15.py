import re
import sys

# Partie lecture de fichier
a = "te.txt"
aa = "input.txt"

lines = []
with open(aa) as f:
	for line in f.readlines():
		lines.append(line.strip())

def manhattan(A, B):
	return abs(B[0] - A[0]) + abs(B[1] - A[1])

# Cette fonction calcul la distance à laquelle le point A est du losange B
# Il calcul suivant l'axe X.
# Elle calcul aussi la distance que parcourera le rayon avant de sortir de B
def rayIntersect(A, B):
	(pos, b, m) = B
	space = m - abs(A[1] - pos[1])
	xIntersect = pos[0] - space # Ou ça va se croiser sur le losange

	distance = xIntersect - A[0]

	# + 1
	if space < 0:
		return (-1, -1)
	return (distance, space * 2) # Attention, distance et space se superpose

# Dit si le point A est dans le losange B et combien il doit parcourir pour sortir de B
def pointInside(A, B):
	man = manhattan(A, B[0])
	if man > B[2]:
		return (False, -1)

	# Si la distance de manhattan est inférieur, il est dedans
	(pos, _, m) = B
	dY = abs(A[1] - pos[1])
	dX = abs(A[0] - pos[0])

	if A[0] < pos[0]:
		return (True, 2 * dX + m - dY - dX)

	return (True, m - (dY + dX))


# Partie parsing
sensors = []
minX = 10
for line in lines:
	# On récup les nombres que l'on veut
	nmbs = [(int(x), int(y)) for (x, y) in re.findall(r'x=(-?\d+), y=(-?\d+)', line)]

	# Dans notre programme, un capteur est une liste avec :
	# Sa position
	# La position de la balise la plus proche
	# Et le "rayon" du losange à l'intérieur duquel il ne peut y avoir de balise
	sensor = (nmbs[0], nmbs[1], manhattan(nmbs[0], nmbs[1]))

	# Ici on calcul le point en X le plus éloigné
	# On récupère la balise la plus éloigné
	if sensor[1][0] < minX:
		minX = sensor[1][0]

	# Ou bien le capteur le plus éloigné
	if sensor[0][0] < minX:
		minX = sensor[0][0]

	sensors.append(sensor)

counter = 0
yL = 2000000
ray = [minX - 10, yL] # -10 par marge de sécurité

it = 0
oneIn = True
while(oneIn):
	d = sys.maxsize
	travel = 0
	se = []

	oneIn = False
	for sensor in sensors:
		(distance, space) = rayIntersect(ray, sensor)

		# La distance peut être négative si on à dépassé le losange
		if distance > 0:
			oneIn = True
			if distance < d and space != 0:
				d = distance
				travel = space
				se = sensor

	# On avance jusqu'a rencontrer le losange le plus proche
	print("Current pos", ray, "Nearest sensor", se, "distance from him", d, "travel through", travel)
	ray[0] += d

	inL = True
	while(inL):
		inL = False
		for sensor in sensors:
			(inside, toTravel) = pointInside(ray, sensor)

			if inside and toTravel != 0:
				inL = True
				ray[0] += toTravel
				counter += toTravel

print(counter)
counter += 1
seee = set()
for sensor in sensors:
	if sensor[1][1] == yL and sensor[1] not in seee:
		seee.add(sensor[1])
		counter -= 1
print(counter)