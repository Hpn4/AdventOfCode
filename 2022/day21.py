import re
from collections import deque
import sympy

# Partie lecture du fichier
a = "te.txt"
aa = "input.txt"

lines = [x.strip() for x in open(0).readlines()]
var = {} # Variables
remaining = [] # Opérations restantes

# Partie 2
root = None
rootOp = ""
humn = 0

for line in lines:
	words = line.split()
	name = words[0][:-1]

	# Partie 2
	if name == "root":
		root = (words[1], words[3])
		rootOp = words[2]
	elif name == "humn":
		humn = int(words[1])

	# Partie 1
	elif len(words) == 2: # Yell a single number
		var[name] = int(words[1])
	else:
		remaining.append((name, words[1], words[2], words[3])) # Yell an expression

def parse(remaining, var):
	pre = 0
	# Si la taille n'a pas changé, c'est qu'on à simplifié au maximum
	while pre != len(remaining):
		i = 0
		pre = len(remaining)
		while i < len(remaining):
			(name, var1, op, var2) = remaining[i]

			if var1 in var and var2 in var:
				var[name] = int(eval(f"{var[var1]} {op} {var[var2]}"))
				remaining.pop(i)
			else:
				i += 1

# Partie 1:
# On fait des copies des opérations restantes à faire et de nos variables
# Puis on ajoute l'opération racine et notre valeur à nouse
remainingClone = remaining[:]
remainingClone.append(("root", root[0], rootOp, root[1]))

varClone = var.copy()
varClone["humn"] = humn

parse(remainingClone, varClone)

# On évalue toute les expressions et le résultat est dans root
print("Partie 1:", varClone["root"])


# Partie 2:
parse(remaining, var) # On simplifie au max notre expression

# Une des valeurs de la racine est statique, on va donc exprimer
# la valeur qu'on ne connais pas en fonction de humn.
# Pour se faire, on part de la valeur en racine inconnue et on va
# remplacer cette variable par son expression. Puis pour la nouvelle expression obtenue,
# on va exprimer chaque variable par sa valeur/expression (si ce n'est pas humn) et ainsi de suite jusqu'à
# compacter notre équation
toTest = root[0] if root[0] in var else root[1] # la valeur statique
expr = root[0] if root[1] in var else root[1] # celle qu'il faut exprimer en fonction de humn

q = deque()
q.append(expr)
while len(q) != 0:
	name = q.popleft()

	for j in range(len(remaining)):
		if remaining[j][0] == name:
			break

	(_, op1, op, op2) = remaining[j]

	# Si on connait la valeur on la remplace
	if op1 in var:
		op1 = var[op1]
	elif op1 != "humn": # Si ce n'est pas humn on continue
		q.append(op1)

	# Si on connait la valeur on la remplace
	if op2 in var:
		op2 = var[op2]
	elif op2 != "humn": # Si ce n'est pas humn on continue
		q.append(op2)

	# L'expression localement simplifié
	e = "(" + str(op1) + str(op) + str(op2) + ")"

	# On remplace l'ancienne variable par son expression simplifié
	expr = expr.replace(name, e)

# Va parser l'expression et la simplifier. Il ne restera plus qu'une expression
# simplifié. Cette expression est convertir sous forme d'objet qui pourra ensuite
# être envoyé à la fonction solve
equation = sympy.sympify(expr)
equation -= var[toTest]

# Cette fonction vq se charcher de résoudre l'équation qu'on lui donne
solution = sympy.solve(equation)

# On affiche la solution
print("Partie 2:", solution[0])
