import re
from collections import deque,defaultdict
from math import log

lines = [x.strip() for x in open(0).readlines()]

snaf = {"0":0, "1":1, "2":2, "-":-1, "=":-2}
def snafuToDec(line):
	n = 0
	p = 1
	for i in range(len(line) - 1, -1, -1):
		n += snaf[line[i]] * p
		p *= 5

	return n

dec = {0:"0", 1:"1", 2:"2", 3:"=", 4:"-"}
def decToSnafu(n):
	sn = ""
	p = 1
	while(n > 0):
		a = n % 5
		if a == 3:
			n += 2
			sn = "=" + sn
		elif a == 4:
			n += 1
			sn = "-" + sn
		else:
			sn = dec[a] + sn

		n = int(n / 5)

	return sn


lines = list(map(lambda x: snafuToDec(x), lines))
a = sum(lines)

print("Partie 1:", a)
print("Partie 2:", decToSnafu(a))