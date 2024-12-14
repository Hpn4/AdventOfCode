import numpy as np

# Can use Z3 also instead of cramer

lines = open(0, "r").read()

acc = [0, 0]
for part in lines.split("\n\n"):
	lines = part.strip().split("\n")
	a, b, c = [line.split(":")[1].strip() for line in lines]

	a = list(map(int, [x.strip()[1:] for x in a.split(",")]))
	b = list(map(int, [x.strip()[1:] for x in b.split(",")]))
	c = list(map(int, [x.strip()[2:] for x in c.split(",")]))

	A = np.array([[a[0], b[0]], [a[1], b[1]]])

	detA = np.linalg.det(A)
	if detA != 0:
		for i,x in enumerate([0, 10000000000000]):
			B = np.array([[c[0] + x, b[0]], [c[1] + x, b[1]]])
			C = np.array([[a[0], c[0] + x], [a[1], c[1] + x]])
			t = np.linalg.det(B) / detA
			u = np.linalg.det(C) / detA

			if t <= 0 or u <= 0 or abs(t - round(t)) > 0.01 or abs(u - round(u)) > 0.01:
				pass
			else:
				acc[i] += round(t) * 3 + round(u)

print("Part1:", acc[0])
print("Part2:", acc[1])
