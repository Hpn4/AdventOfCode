import re

# Partie lecture fichier + parsing
a = "te.txt"
aa = "input.txt"

blueprints = []
for line in open(aa).readlines():
	nmbs = [int(x) for x in re.findall(r'\d+', line.strip())]

	blueprints.append(tuple(nmbs[1:]))

# Le nombre maximal de geode qu'on pourrait produire :
# Le nombre actuel de geode + le nombre de robot geode * le temps qu'il reste
# Cette partie donne la première approximation.
# Ensuite on peut peut-être produire des géodes durant le temps qu'il reste.
# Mais on va probablement pas produire de robot géode à chaque minute.
# On a posé arbitrairement qu'on en produit un toutes les 2min
def opt(m, q, t):
	return m + (q + t // 2) * t

g = [0]
seen = set()
def getMax(blueprint, ressources, robots, time):
	(oreR, clayR, obsidianROre, obsidianRClay, geodeROre, geodeRObs) = blueprint

	# Max cost for each ressources
	cost = [max(oreR, clayR, obsidianROre, geodeROre), obsidianRClay, geodeRObs, float('inf')]
	for i in range(len(ressources)):
		# Si on produit plus de resources que nécessaire => foireux
		if robots[i] > cost[i]:
			return 0

		ressources[i] = min(ressources[i] + robots[i], time * cost[i] - robots[i] * (time - 1))

	if opt(ressources[3], robots[3], time) <= g[0]:
		return 0

	if time == 0:
		g[0] = max(g[0], ressources[3])
		return ressources[3]

	label = time, tuple(ressources), tuple(robots)
	if label in seen:
		return 0

	m = 0
	seen.add(label)

	if ressources[0] >= geodeROre and ressources[2] >= geodeRObs: # geode robots
		resClone = ressources[:]
		robotsClone = robots[:]
		robotsClone[3] += 1
		resClone[0] -= geodeROre
		resClone[2] -= geodeRObs
		resClone[3] -= 1
		m = max(m, getMax(blueprint, resClone, robotsClone, time - 1))

	if ressources[0] >= obsidianROre and ressources[1] >= obsidianRClay: # obsidian robots
		resClone = ressources[:]
		robotsClone = robots[:]
		robotsClone[2] += 1
		resClone[0] -= obsidianROre
		resClone[1] -= obsidianRClay
		resClone[2] -= 1
		m = max(m, getMax(blueprint, resClone, robotsClone, time - 1))

	if ressources[0] >= clayR: # clay robots
		resClone = ressources[:]
		robotsClone = robots[:]
		robotsClone[1] += 1
		resClone[0] -= clayR
		resClone[1] -= 1
		m = max(m, getMax(blueprint, resClone, robotsClone, time - 1))

	if ressources[0] >= oreR: # ore robots
		resClone = ressources[:]
		robotsClone = robots[:]
		robotsClone[0] += 1
		resClone[0] -= oreR + 1
		m = max(m, getMax(blueprint, resClone, robotsClone, time - 1))

	return max(m, getMax(blueprint, ressources[:], robots[:], time - 1))

def getM(blueprint):
	seen = set()
	return getMax(blueprint, [-1, 0, 0, 0], [1, 0, 0, 0], 24)

p1 = 0
for i in range(len(blueprints)):
	seen = set()
	g = [0]

	geode = getMax(blueprints[i], [-1, 0, 0, 0], [1, 0, 0, 0], 24)

	p1 += (i + 1) * geode

print("Partie 1:", p1)

p2 = 1
for bp in blueprints[:3]:
	seen = set()
	g = [0]

	geode = getMax(bp, [-1, 0, 0, 0], [1, 0, 0, 0], 32)

	p2 *= geode

print("Partie 2,", p2)