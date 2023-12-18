import sys

lines = open(sys.argv[1], "r").readlines()

dirs = {'U': (0, -1), 'L': (-1, 0), 'R': (1, 0), 'D': (0, 1)}
colD = "RDLU"

def decode(color):
	color = color[2:-1]

	d = int(color[:5], 16)
	dire = colD[int(color[-1])]
	
	return d,dire

def move(x, y, pos, d, area, p):
	accX, accY = dirs[pos]
	prevX, prevY = x, y
	x += accX * d
	y += accY * d

	area += (x + prevX) * (y - prevY)

	return x, y, area, p + d

p, area, x, y = 0, 0, 0, 0
p2, area2, x2, y2 = 0, 0, 0, 0
for line in lines:
	pos, d, color = line.split()

	# Part 1
	x, y, area, p = move(x, y, pos, int(d), area, p)

	# Part 2
	d, pos = decode(color)
	x2, y2, area2, p2 = move(x2, y2, pos, d, area2, p2)

print(abs(area // 2) + p//2 + 1)
print(abs(area2 // 2) + p2//2 + 1)