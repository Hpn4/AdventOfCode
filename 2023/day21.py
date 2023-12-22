import sys
import helper

lines, h, w = helper.read(sys.argv[1], lines=True)

start = helper.findGrid(lines, "S")

def run(pos, prec, steps):
	for i in range(prec, steps):
		moved = set()

		for x,y in pos:
			def f(x1, y1):
				if lines[y1 % h][x1 % w] != '#':
					moved.add((x1, y1))

			helper.doEachDir(lines, x, y, f, check=False)

		pos = moved

	return pos

pos = set([start])

def black_magic(n):
	s = (w - 1) // 2

	s0 = run(pos, 0, s)
	a0 = len(s0)

	s1 = run(s0, s, s + w)
	a1 = len(s1)

	s2 = run(s1, s + w, s + w * 2)
	a2 = len(s2)

	return round(helper.interp([0, 1, 2], [a0, a1, a2], n))

print("Part1:", len(run(pos, 0, 64)))
print("Part2:", black_magic(26501365//w))