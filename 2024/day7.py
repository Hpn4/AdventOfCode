lines = open(0, "r").readlines()

# Forward (start from first number and go to res), naive but lots of branches
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

# Backward (start from res and go back to start), allow early prunning
def test2(res, n, pos, p2=False):
	if pos <= 0:
		return n[0] == res

	nmb, r = n[pos], False

	# Early prunning if negative
	if res - nmb > 0:
		r = test2(res - nmb, n, pos - 1, p2)

	# Early prunning if not a multiple
	if res % nmb == 0:
		r |= test2(res // nmb, n, pos - 1, p2)

	# Early prunning if not concatenate
	s_res, s_n = str(res), str(nmb)
	if p2 and s_res != s_n and s_res.endswith(s_n):
		r |= test2(int(s_res[:-len(s_n)]), n, pos - 1, p2)

	return r

acc = 0
acc2 = 0
for line in lines:
	res,n = line.split(":")
	res = int(res)
	n = list(map(int, n.split()))

	if test2(res, n, len(n) - 1):
		acc += res

	if test2(res, n, len(n) - 1, True):
		acc2 += res

print("Part1:", acc)
print("Part2:", acc2)
