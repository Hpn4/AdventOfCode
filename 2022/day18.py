from queue import Queue

# Partie lecture + parsing du fichier
a = "te.txt"
aa = "input.txt"

# Partie lecture de fichier et parsing
lines = list(map(lambda l: l.strip(), open(aa).readlines()))

cubes = {}
for line in lines:
	cubes[tuple(map(lambda x: int(x), line.split(",")))] = True

delta = [-1, 1]
faces = 0
for (x, y, z) in cubes.keys():
	for dx in delta:
		if not (x + dx, y, z) in cubes:
			faces += 1
	
	for dy in delta:
		if not (x, y + dy, z) in cubes:
			faces += 1
	
	for dz in delta:
		if not (x, y, z + dz) in cubes:
			faces += 1

print("Partie 1:", faces)

# Partie 2
q = Queue()
visited = {(20, 20, 20):True}
q.put((20, 20, 20))
faces = 0

minB = -6
maxB = 25
while not q.empty():
	(x, y, z) = q.get()

	for dx in delta:
		idd = (x + dx, y, z)
		if idd in cubes:
			faces += 1
		elif (not idd in visited) and minB <= x + dx < maxB:
			visited[idd] = 1
			q.put(idd)

	for dy in delta:
		idd = (x, y + dy, z)
		if idd in cubes:
			faces += 1
		elif (not idd in visited) and minB <= y + dy < maxB:
			visited[idd] = 1
			q.put(idd)

	for dz in delta:
		idd = (x, y, z + dz)
		if idd in cubes:
			faces += 1
		elif (not idd in visited) and minB <= z + dz < maxB:
			visited[idd] = 1
			q.put(idd)

print("Partie 2:", faces)