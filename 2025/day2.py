
lines = open("input2.txt").read().strip()

acc = 0
for rang in lines.split(","):
	rang = rang.strip()

	a, b = rang.split("-")

	for i in range(int(a), int(b) + 1):
		num = str(i)

		for j in range(1, len(num)):
			chunks = [num[i:i+j] for i in range(0, len(num), j)]
			equal = True
			prev = chunks[0]
			for k in range(1, len(chunks)):
				if chunks[k] != prev:
					equal = False

			if equal:
				acc += i
				break

print(acc)
