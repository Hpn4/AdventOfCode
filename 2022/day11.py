import re

modulus = 1

# J'ai crée une class pour que ce soit plus simple d'enregistrer toutes les informations
# sur les donnéees des singes
class Monkey:

	def __init__(self, mid, items, operand, multiply, divisibility, monkeyTrue, monkeyFalse):
		self.items = items
		self.mid = mid
		self.operand = operand
		self.multiply = multiply
		self.divisibility = divisibility
		self.monkeyTrue = monkeyTrue
		self.monkeyFalse = monkeyFalse
		self.counter = 0

	def calculate(self, item):

		if self.operand == None:
			item *= item
		elif self.multiply:
			item *= self.operand
		else:
			item += self.operand

		# Partie 1 : 
		# return int(item / 3)

		# C'est cette ligne qui permet à la partie 2 d'être rapide.
		# En fait on a pas besoin d'avoir la véritable valeur de chaque chiffre, ce qui nous
		# interesse c'est de savoir si c'est divisible par les valeurs de singes.
		return item % modulus

	# PEtite fonction pour simplement ajouter un item
	def addItem(self, item):
		self.items.append(item)

	def treatAllItems(self, monkeys):
		i = 0
		while i < len(self.items):
			calculated = self.calculate(self.items[i])
			self.counter += 1

			if calculated % self.divisibility == 0:
				monkeys[self.monkeyTrue].addItem(calculated)
				#print(self.mid, "Send", calculated, "to", self.monkeyTrue)
			else:
				monkeys[self.monkeyFalse].addItem(calculated)
				#print(self.mid, "Send", calculated, "to", self.monkeyFalse)

			i += 1

		self.items = []


file = open("input.txt", "r")

lines = file.readlines()
monkeys = []

# On va parser notre fichier
for i in range(len(lines)):
	if lines[i].startswith("Monkey"):
		# Monkey ID
		nmbs = [int(s) for s in re.findall(r'\d+', lines[i])]
		monkeyId = nmbs[0]

		# Monkey items
		i += 1
		items = [int(s) for s in re.findall(r'\d+', lines[i])]

		# Operation
		i += 1
		nmbs = [int(s) for s in re.findall(r'\d+', lines[i])]
		# i il n'y a pas de nombre c'est qu'on fait le produit old * old
		operand = nmbs[0] if len(nmbs) == 1 else None

		# Si il y a un nombre, on regarde si il y a le sine * dans la string.
		# Si c'est le cas on effectue la multiplication old * operand
		# Sinon on fait old + operand
		multiply = True if "*" in lines[i] else False

		# Divisibility
		i += 1
		nmbs = [int(s) for s in re.findall(r'\d+', lines[i])]
		divisibility = nmbs[0]

		# To send
		i += 1
		nmbs = [int(s) for s in re.findall(r'\d+', lines[i])]
		monkeyTrue = nmbs[0]

		i += 1
		nmbs = [int(s) for s in re.findall(r'\d+', lines[i])]
		monkeyFalse = nmbs[0]

		m = Monkey(monkeyId, items, operand, multiply, divisibility, monkeyTrue, monkeyFalse)
		monkeys.append(m)

		# Notre modulo de simplification est le produit des tests de divisibilité des singes
		# C'est un peu compliqué à expliquer pk ça marche mathématiquement.
		# Mais grosso modo, si tu veux savoir qu'un nombre est divisible par une certaine valeur
		modulus *= divisibility

turn = 0
while turn < 10000:
	for m in monkeys:
		m.treatAllItems(monkeys)

	turn += 1

counters = []
for m in monkeys:
	counters.append(m.counter)

print(counters)
counters.sort()
print(counters[-1] * counters[-2])