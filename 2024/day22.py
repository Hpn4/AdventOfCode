import sys
from collections import deque, defaultdict

lines = open(sys.argv[1], "r").readlines()

D = defaultdict(list)
def solve(secret):
	Q = deque([0,0,0,0], maxlen=4)
	SEEN = set()
	prev = secret % 10
	for i in range(2000):
		secret = (secret * 64) ^ secret
		secret = secret % 16777216

		secret = (secret // 32) ^ secret
		secret = secret % 16777216

		secret = (secret * 2048) ^ secret
		secret = secret % 16777216

		e = secret % 10
		Q.append(e - prev)
		prev = e

		# Register only when queue full and part2 stop one iteration before part1
		if i >= 3 and i != 1999:
			key = (Q[0], Q[1], Q[2], Q[3])
			if key in SEEN:
				continue

			SEEN.add(key)
			D[key].append(e)

	return secret

# Part1
acc = 0
for line in lines:
	secret = int(line.strip())
	acc += solve(secret)

# Part2
acc2 = 0
for k,v in D.items():
	m = sum(v)
	acc2 = max(acc2, m)

print("Part1:", acc)
print("Part2:", acc2)