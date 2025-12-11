import numpy as np
from collections import deque
from ortools.sat.python import cp_model

MAX_BUT_P1 = 8
MAX_P2_RANGE = 200

lines = open("input10.txt").readlines()
mach = []

for line in lines:
	line = line.strip()

	# Lights
	li, re = line.split("]")
	li = [0 if x == "." else 1 for x in li[1:]]
	li = np.array(li)

	# Buttons
	but, re = re.split("{")
	but = [[int(x) for x in b[1:-1].split(",")] for b in but.split()]

	# Jolt
	jolt = [int(x) for x in re[:-1].split(",")]

	mach.append((li, but, jolt))

def h_(arr):
	return "".join([str(x) for x in arr])

def solve(li, but):
	current = np.zeros_like(li)
	Q = deque()
	Q.append((current, 0))
	H = {h_(current): 0}

	while Q:
		curr, count = Q.pop()
		key = h_(curr)

		for i in range(len(but)):

			b = but[i]
			c = curr.copy()
			c[b] ^= 1

			if count + 1 >= MAX_BUT_P1:
				continue

			key2 = h_(c)
			if key2 not in H or count + 1 < H[key2]:
				Q.append((c, count + 1))

			if key2 not in H or count + 1 < H[key2]:
				H[key2] = count + 1

	return H[h_(li)]

def solve2(jolt, but):
    model = cp_model.CpModel()
    n = len(but)
    m = len(jolt)

    x = [model.NewIntVar(0, MAX_P2_RANGE, f'x{i}') for i in range(n)]

    A = []
    for b in but:
        a = [0]*m
        for idx in b:
            a[idx] = 1
        A.append(a)
    A = np.array(A).T

    for i in range(m):
        model.Add(sum(A[i][j]*x[j] for j in range(n)) == jolt[i])

    model.Minimize(sum(x))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        solution = [solver.Value(xi) for xi in x]
        return sum(solution)


acc = 0
acc2 = 0
for i,(li, but, jolt) in enumerate(mach):
	res = solve(li, but)
	res2 = solve2(jolt, but)
	#print(f"{i}/{len(mach)} {res} {res2}")
	acc += res
	acc2 += res2

print("Part1:", acc)
print("Part2:", acc2)
