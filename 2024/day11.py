from collections import defaultdict

line = open(0, "r").readlines()[0].strip()

stones = {key: 1 for key in map(int, line.split())}

def run(stones, step):
	for i in range(step):
		stone = defaultdict(int)

		for k,v in stones.items():
			if k == 0:
				stone[1] += v
			elif len(str(k)) % 2 == 0:
				ks = str(k)
				l = int(ks[:len(ks) // 2])
				r = int(ks[len(ks) // 2:])
				stone[l] += v
				stone[r] += v
			else:
				kk = k * 2024
				stone[kk] += v

		stones = dict(stone)

	return stones, sum(stones.values())

stones, acc = run(stones, 25)
print("Part1:", acc)
print("Part2:", run(stones, 50)[1])