from collections import defaultdict, deque
import heapq
import sys
from helper import findGrid, DIRS

lines = open(sys.argv[1], "r").readlines()
grid = [[c for c in line.strip()] for line in lines]

sx,sy = findGrid(grid, "S")
ex,ey = findGrid(grid, "E")

class Item:
    def __init__(self, s, x,y,d,path):
        self.d = d
        self.s = s
        self.x = x
        self.y = y
        self.path = path

    def __lt__(self, other):
        # Define the comparison logic
        return self.s < other.s

def solve(PATH):
	Q = []
	heapq.heappush(Q, Item(0,sx,sy,0,dict()))
	SEEN = set()
	DD = dict()
	best = None
	while Q:
		az= heapq.heappop(Q)
		s,x,y,d,path = az.s, az.x, az.y, az.d, az.path
		path[(x,y)] = s

		if (d,x,y) not in DD:
			DD[(d,x,y)] = s

		if (x,y) in PATH and PATH[(x,y)] == s:
			for k,v in path.items():
				PATH[k] = v

		if x == ex and y == ey and (best is None or best == s):
			best = s
			for k,v in path.items():
				PATH[k] = v

		if (d,x,y) in SEEN:
			continue

		SEEN.add((d,x,y))

		dx,dy = DIRS[d]
		xx = x + dx
		yy = y + dy

		if grid[yy][xx] != "#":
			heapq.heappush(Q, Item(s+1, xx,yy,d, path.copy()))
		
		heapq.heappush(Q, Item(s + 1000, x,y, (d + 1) % 4, path.copy()))
		heapq.heappush(Q, Item(s + 1000, x,y, (d + 3) % 4, path.copy()))

	return best

PATH = dict()

print("Part1:", solve(PATH))
solve(PATH)
solve(PATH)

print("Part2:", len(PATH))
