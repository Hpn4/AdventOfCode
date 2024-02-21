import time
file = open("input.txt", "r")

lines = file.readlines()

acc = 0
j = 0

t = time.time()
while j < len(lines):
	l1 = lines[j].strip()
	l2 = lines[j + 1].strip()
	l3 = lines[j + 2].strip()

	i = 0
	p = 0
	while i < len(l1) and p == 0:
		c = l1[i]
		if c in l2 and c in l3:
			if c.isupper():
				p += 26 + ord(c) - ord('A') + 1
			else:
				p += 1 + ord(c) - ord('a')
		i += 1

	acc += p
	j += 3

print(acc)
print(time.time() - t)
t = time.time()
p = 0
j = 0
while j < len(lines):
	h = [0 for _ in range(26)]
	H = [0 for _ in range(26)]

	for i in range(3):
		h1 = [0 for _ in range(26)]
		H1 = [0 for _ in range(26)]
		line = lines[j + i].strip()
		for c in line:
			if c.isupper():
				H1[ord(c) - ord('A')] += 1
			else:
				h1[ord(c) - ord('a')] += 1

		for k in range(len(H1)):
			if H1[k] > 0:
				H[k] += 1
			if h1[k] > 0:
				h[k] += 1

	i = 0
	find = 0
	while i < len(H) and find == 0:
		if H[i] == 3:
			find = 26 + i + 1
		elif h[i] == 3:
			find = i + 1
		i += 1

	p += find
	j += 3


print(p)
print(time.time() - t)