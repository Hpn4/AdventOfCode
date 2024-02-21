import re

a = "te.txt"
aa = "input.txt"
file = open(aa, "r")

lines = file.readlines()

# Dans la première partie, mettre à 4 sinon à 14
paternSize = 14

# J'ai mis dans une boucle for parce que j'ai testé plusieurs
# exemples qu'ils nous ont donnée
for line in lines:
	i = 0

	# La technique que j'ai utilisé est assez utile pour ce genre de problème.
	# Je vais construire ce qu'on appelle un histogramme. Un histogramme est une liste
	# (ici de 26 en taille car il y a 26 caractères dans l'alphabet) initialisé à 0.
	# Puis je parcours la longueur du pattern en partant de i.
	# Et pour chaque caractère, je lui associe une case dans l'histogramme
	# avec le même système qu'il y a deux jours :
	# 97 <= ord(X) <= 122				lorsque X est une minuscule
	# 0 <= ord(X) - ord('a') <= 25		lorsque X est une minuscule
	while i < len(line):
		# On initialise l'histogramme
		h = [0 for _ in range(26)]

		# On le remplit
		for j in range(paternSize):
			h[ord(line[i + j]) - ord('a')] += 1

		j = 0
		# On parcours l'histogramme tant qu'on a pas trouvé de case ou la valeur est strictement
		# supérieur à un
		while j < 26 and h[j] <= 1:
			j += 1
		
		# Si cette condition est rempli, ça veut dire qu'on est sortie de la boucle while par j < 26
		# et non la deuxième condition. Nous avons donc parcouru l'entièreté de l'histogramme sans détecté
		# de doublon
		if j >= 26:
			# On veut afficher la fin du pattern
			print(i + paternSize)
			break

		i += 1
