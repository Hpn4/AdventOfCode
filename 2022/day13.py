import re
import functools

# Partie lecture de fichier
a = "te.txt"
aa = "input.txt"

lines = []
with open(aa) as f:
	for line in f.readlines():
		lines.append(line.strip())

# Cette fonction va juste exraire un nombre dans la liste l à l'index i
# Elle renvoi le nombre et le nouveau i.
# Le nouveau i car il peut y avoir des nombres à 2 chiffres
def getNumberToken(l, i):
	nmb = ""

	while i < len(l) and l[i].isdigit():
		nmb += l[i]
		i += 1

	return (int(nmb), i)

# Cette fonction va transformer notre string en une liste de token plus facilement
# manipulable.
# Dans cette liste, il n'y aura que des "[", des "]" et des nombres
def tokenizeLine(l):
	T = []

	i = 0
	while i < len(l):
		if l[i] == "[":
			T.append("[")
			i += 1
		elif l[i] == "]":
			T.append("]")
			i += 1
		elif l[i].isdigit():
			(nmb, i) = getNumberToken(l, i)
			T.append(nmb)
		else: # Virgule, on s'en fout
			i += 1

	return T

# C'est le coeur du programme, elle va comparer deux listes de tokens
# Renvoie 1 si mal trié
# Renvoie -1 si bien trié
# C'est un peu bizarre comme valeur de retour, mais c'est pour la partie 2,
# tu verras en lisant plus bas
def compare(l, r):
	left = l.copy()
	right = r.copy()

	i = 0
	good = True
	while(True):
		# On entre dans une liste à gauche
		if left[i] == "[":
			# Si à droite on entre dans une liste, tout va bien, on avance dans le parsing
			if right[i] == "[":
				i += 1
			# Si on a un nombre, on le transforme en une liste. On fait cela en ajoutant les tokens
			# "[" et "]" avant et après le nombre. Comme ça au prochain tour de boucle, la conditon d'au dessu
			# sera remplie. C'est pour cela que j'incremente pas i car après cette conditon right[i] = "["
			elif type(right[i]) == int:
				right.insert(i, "[")
				right.insert(i + 2, "]")
		
		# On entre dans une liste à droite
		elif right[i] == "[":
			# Si on a un nombre, on le transforme en une liste
			if type(left[i]) == int:
				left.insert(i, "[")
				left.insert(i + 2, "]")

		# Fin de liste à gauche
		if left[i] == "]":
			if right[i] == "]":
				i += 1
			else: # Plus d'élements à gauche
				return -1

		# Plus d'élements à droite
		if right[i] == "]" and left[i] != "]":
			return 1

		# Si on a deux nombres
		elif type(left[i]) == int and type(right[i]) == int:
			if left[i] == right[i]: # Egaux, tout va bien on avance
				i += 1
			elif left[i] < right[i]: # Celui de gauche est inférieur, c'est bien trié
				return -1
			else: # Sinon c'est mal trié
				return 1

	return -1


tokens = []
acc = 0
j = 0
while j < len(lines):
	left = tokenizeLine(lines[j])
	right = tokenizeLine(lines[j + 1])

	tokens.append(left)
	tokens.append(right)

	j += 3
	if compare(left, right) == -1:
		acc += int(j / 3)

# We add divider packets
divider1 = tokenizeLine("[[2]]")
divider2 = tokenizeLine("[[6]]")

tokens.append(divider1)
tokens.append(divider2)

# Ensuite on va trier nos élements. En fait pour trier une liste d'élements, on peut
# utiliser une fonction qu'on à codé nous même. Il faut que les valeurs renvoyés soit des entiers
# La je demande à trier mes tokens en fonction de compare. Qui est la fonction qui dit si oui
# ou non deus liste sont dans le bon ordre
sortedTokens = sorted(tokens, key=functools.cmp_to_key(compare))

# Je rajoute + 1 car les listes sont en bases 0
index = (sortedTokens.index(divider1) + 1) * (sortedTokens.index(divider2) + 1)


print("Partie 1:", acc)
print("Partie 2:", index)