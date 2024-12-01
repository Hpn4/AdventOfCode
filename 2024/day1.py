lines = open(0, "r").readlines()

acc = 0
acc2 = 0

l1 = []
l2 = []
for line in lines:
	a,b = line.split()

	l1.append(int(a))
	l2.append(int(b))

l1 = sorted(l1)
l2 = sorted(l2)

acc = sum(abs(l1[i] - l2[i]) for i in range(len(l1)))

for a in l1:
	acc2 += a * sum(a == b for b in l2)

print("Part1:", acc)
print("Part2:", acc2)