import re

# J'ai décidé de passer par une structure en arbre parce que je ne savais pas
# si on revenait dans un meme dossier plusieurs fois.
# Un arbre est une structure de donnée avec une racine qui porte une valeur
# (ici le nom du répertoire et sa taille) et possède plusieurs fils qui sont eux aussi des arbres.
# C'est une structure de donnée recursive
class Tree:

	def __init__(self, value, childs, size):
		self.value = value
		self.childs = childs
		self.size = size

	# Pour simplifier le cd ..
	# j'ai ajoute le champs parent qui indique quel arbre est le père de notre arbre actuel
	def addChilds(self, c):
		if c not in self.childs:
			self.childs.append(c)
			c.parent = self # Je défini le père de l'enfant


a = "te.txt"
aa = "input.txt"
file = open(aa, "r")

lines = file.readlines()

# On initialise notre arbre racine et définit lui même comme parent
# pour eviter des cd .. en /
root = Tree("/", [], 0)
root.parent = root

# On va travailler avec cette arbre
current = root

for line in lines:
	line = line.strip()

	if line.startswith("$ cd"):
		line = line[5:]

		if line == '/':
			current = root
		elif line == '..':
			# On revient d'un dossier en arrière donc on remonte dans l'arbre
			# On aurait d'ailleurs ici pu mettre à jour la taille de current.parent
			current = current.parent
		else:
			# On crée un nouvel arbre enfant et on l'ajoute à notre arbre actuel
			t = Tree(line, [], 0)
			current.addChilds(t)

			# On change de dossier
			current = t
	elif line[0] != "$":
		if not line.startswith("dir"):
			# On récupère juste la taille et on l'ajoute à celle de notre arbre actuel
			line = line.split(' ')
			current.size += int(line[0])

# Part 1
# Ici je fais ce qu'on appelle un parcours profondeur.
# Il y a 2 grandes manières de parcourir les arbres : le parcours profondeur et largeur
# Le parcrours profondeur est de nature récursive est fonctionne comme suit :
# 
# def parcoursProfondeur(arbre):
# 	# Traitement Préfixe
# 
# 	pour tout les enfants c dans l'arbre:
# 		# Traitement infixe/intermédiaire
# 		parcoursProfondeur(c)
# 		# Traitement infixe/intermédiaire
# 	
# 	# Traitement suffixe
# 
# Les commentaires avec les traitements sont les opérations que l'on peut effectuer.
# Grosso modo leur signification c'est :
# Prefixe: fait qqc avant d'aller explorer des enfants et d'aller trop loin dans la récursion
# Infixe: fait qqc entre deux enfant
# Suffixe: fait qqc lorsqu'on remonte de la récursion
# 
# Il est appeller parcours profondeur parce qu'on vois qu'il va aller chercher le plus loin possible.
# 
def getTreeSize(tree):
	size = tree.size

	l = 0
	for c in tree.childs:
		# Notre traitement infixe est de mettre à jour la taille
		# Et aussi la taille potentiels des dossiers pas trop lours
		l += getTreeSize(c)
		size += c.size

	# Ce n'est qu'en remontant la récursion qu'on test si le dossier est pas trop lourd
	tree.size = size
	if tree.size < 100000:
		l += tree.size

	return l

print("Part 1:", getTreeSize(root))

# Part 2
# On calcule l'espace nécessaire
space = 70000000
space -= root.size
needed = 30000000 - space

# Même système que la partie 1 (en fait la plupart des opérations sur les arbres se font avec des parcours
# profondeur et quelques fois largeur)
def findBigEnoughDir(n, m, tree):
	for c in tree.childs:
		m = findBigEnoughDir(needed, m, c)

	if tree.size >= n and tree.size < m:
		m = tree.size

	return m

print("Part 2:", findBigEnoughDir(needed, root.size + 1, root))

# Je suis passé par des arbres, mais en réalité une pile suffisait (c'est comme une pile d'assiette).
# Une pile est une structure de donnée avec trois opérations :
#  - peek: regarde le premier élement de la pile sans le supprimer (on regarde l'assiette)
#  - push: rajoute un élement sur la pile (on met une assiète en plus)
#  - pop:  on enlève le premier élement (on retire l'assiette tout en haut de la pile)
# 
# Dans une pile, on ne peut accèder qu'à un seul élement, celui qui est au plus haut de la pile.
# Elles sont aussi appellé des LIFO pour Last In First Out.
# En effet l'élement qu'on va pop sera celui qu'on viendra tout juste de mettre.
# Les piles sont utilisé dans de nombreux domaines. La récursivité, en Python ou même en C est une pile,
# on peut faire des tests de parenthésages avec une pile, bref..
# 
# L'idée avec une pile pour ajd c'est parce qu'en fait on ne se soucie que de l'endroit ou on est pour ajouter
# la taille.
# Et remonter dans la hièrarchie consiste en fait à pop la taille. Puis on peut directement mêttre à jour
# la taille du père en popant le dernière élement et ajoutant cette taille au nouveau premier élement de la
# pile.
# 
# Mais bon, j'aime bien les arbres et je trouve ça plus clair. Puis c'est une structure vraiment puissante
# et énormement utilisé en informatique