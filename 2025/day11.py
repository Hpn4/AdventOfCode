
lines = open("input11.txt").readlines()

cables = {}
for line in lines:
	line = line.strip()

	key, vals = line.split(":")
	vals = vals.split()

	cables[key] = vals

M = {}

def solve(n, fft_seen, dac_seen):
	key = (n, fft_seen, dac_seen)
	if key in M:
		return M[key]

	if n == "out":
		return 1 if fft_seen and dac_seen else 0

	fft_seen |= n == "fft"
	dac_seen |= n == "dac"

	key = (n, fft_seen, dac_seen)

	fft_ = fft_seen
	dac_ = dac_seen

	acc = 0
	for next_ in cables[n]:
		acc += solve(next_, fft_seen, dac_seen)

	M[key] = acc
	return acc

print("Part1:", solve("you", True, True))
print("Part2:", solve("svr", False, False))
