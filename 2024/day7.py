lines = open(0, "r").readlines()

def test(res, n, pos, acc, p2=False):

	if acc > res:
		return False

	if pos >= len(n):
		return res == acc

	r = test(res, n, pos + 1, acc + n[pos], p2)
	r |= test(res, n, pos + 1, acc * n[pos], p2)

	if p2:
		r |= test(res, n, pos + 1, int(str(acc) + str(n[pos])), p2)

	return r

acc = 0
acc2 = 0
for line in lines:
	res,n = line.split(":")
	res = int(res)
	n = list(map(int, n.split()))

	if test(res, n, 1, n[0]):
		acc += res

	if test(res, n, 1, n[0], True):
		acc2 += res

print("Part1:", acc)
print("Part2:", acc2)