import re
from collections import deque

# Partie lecture fichier + parsing
a = "te.txt"
aa = "input.txt"

lines = list(map(lambda l: l.strip(), open(aa).readlines()))

nmbs = [int(x) for x in lines]
nmbs = [x * 811589153 for x in nmbs]
nmbs = deque(list(enumerate(nmbs)))


# -12161663457705
for t in range(10):
	for i in range(len(nmbs)):
		while nmbs[0][0]!=i:
			nmbs.append(nmbs.popleft())

		val = nmbs.popleft()
		to_pop = val[1]
		to_pop %= len(nmbs)

		for _ in range(to_pop):
			nmbs.append(nmbs.popleft())
		nmbs.append(val)
	
#print(nmbs)
for j in range(len(nmbs)):
    if nmbs[j][1] == 0:
        break

s = nmbs[(j+1000)%len(nmbs)][1] + nmbs[(j+2000)%len(nmbs)][1] + nmbs[(j+3000)%len(nmbs)][1]
print(s)