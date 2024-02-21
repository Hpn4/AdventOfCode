import re

a = "te.txt"
aa = "input.txt"
file = open(aa, "r")

lines = file.readlines()
acc = ""

# On lit les piles depuis le fichier
crates = [[] for _ in range(9)]
i = 0
while not lines[i].startswith(" 1"):
	line = lines[i][:-1] # Supprime \n

	for j in range(len(line)):
		# Si on est sur une majuscule
		if line[j].isupper():
			# On divise par 4 l'index car chaque majuscule est dans un pattern du type :
			# " [X]" où X est notre majuscule
			crates[int(j / 4)].append(line[j])
	i += 1

# Je met à l'envers les arrays pour pouvoir ainsi ajouter les élements à la
# fin. De même il seront supprimé de la fin lorsqu'ils bougeront.
# Le raisonnement inverse est possible, avec des insert(0, pop(0)) comme toi tu as fait.
# Mais insert(0) et pop(0) sont en complexité O(n) c'est à dire qu'ils dependent
# de la taille de la liste et sont donc de plus en plus couteux en temps au fur et à mesure
# que la liste grossit.
# Car pour pop(0) ce qu'il se cache derrière c'est : prendre le premier élément, le décaler jusqu'a
# la fin et ensuite le supprimer. Donc tu parcours complètement l'array.
# De même pour insert(0), on ajoute l'élémenet à la fin et on le ramène jusqu'au début.
# Si ça t'intéresse de savoir pourquoi ça marche comme ça, je pourrais prendre le temps
# de t'expliquer
# 
# D'ajouter directement à la fin ou de supprimer à la fin est donc une opération
# "presque" instantannée (presque car si la liste est trop petite, python va allouer un espace
# mémoire 2x plus grand et recopier les éléments. Mais vue qu'il double la capacité à chaque fois,
# plus on ajoute d'éléments et moins cette opération se produit).
# Donc append(x) et pop() sans paramètre sont en complexité O(1).
# c'est à dire constant (ils ne dépendent d'aucune autre variable).
# Pour des petites arrays la diférence de temps est à peine notable,
# mais sur des données plus grandes, c'est un élement à prendre en compte.
for c in crates:
	c.reverse()

print(crates)

# On se place à la première instruction move (il y a la ligne des numéros + la ligne vide)
i += 2

while i < len(lines):
	line = lines[i].strip()

	# On recup les nombres qu'il nous faut
	nmbs = [int(s) for s in re.findall(r'\d+', line)]

	# On les ajoute successivement au bon endroit
	for j in range(nmbs[0]):
		crates[nmbs[2] - 1].append(crates[nmbs[1] - 1].pop())

	# Pour la partie 2, il suffit de pop(-(nmbs[0]-j)) j fois
	# Il y a bien mieux car pop(i) n'est pas super comme expliqué plus haut.
	# 
	# Une autre solution serait d'avoir des stacks d'une taille fixe initialisé avec une valeur comme:
	# stacks = [['0' for _ in range(n)] for _ in range(9)] ou n est le nombre maximum d'élément dans un stack
	# Le nombre maximum est simplement le nombre de toutes les lettres des stacks.
	# 
	# Ensuite pour chaque stack on garde en mémoire un indice correspondant au dernier élément :
	# index = [0 for _ in range(9)]
	# ainsi pour supprimer, on ne pop pas, on diminue notre indice de dernier element,
	# par exemple pour supprimer 3 élément dans la stack 1: index[0] -= 3
	# Et pour ajouter une valeur à la fin de la stack 1:
	# stacks[0][index[0]] = e
	# Ou e est l'élément à ajouter.
	# 
	# On n'a pas besoin de pop ou de supprimer réellement les élements car on réecrit à chaque fois
	# par dessus et on ne s'interesse pas à ce qu'il y a après notre indice de dernier élement.
	# 
	# Mais bon encore une fois, les listes sont très petites alors ce genre d'optimisation est à peine
	# notable.

	i += 1

# Vue que nos arrays sont à l'envers, on récupère les élements à la fin et non au début.
for c in crates:
	acc += c[-1]

print(acc)