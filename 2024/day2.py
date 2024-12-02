lines = open(0, "r").readlines()

def safe(n):
	d = True
	inc = True

	for i in range(len(n) - 1):
		diff = abs(n[i] - n[i + 1])
		if diff < 1 or diff > 3:
			return False

		if n[i] > n[i + 1]:
			inc = False
		else:
			d = False

	if d or inc:
		return True

	return False

acc = 0
acc2 = 0

for line in lines:
	e = [int(x) for x in line.split()]

	for j in range(len(e)):
		n = [x for x in e]
		del n[j]
		
		if safe(n):
			acc2 += 1
			break

	acc += safe(e)

print("Part1:", acc)
print("Part2:", acc2)