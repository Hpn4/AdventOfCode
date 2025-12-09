from shapely.geometry import Polygon, box
from shapely.prepared import prep

lines = open("input9.txt").readlines()

point = [[int(x) for x in line.strip().split(",")] for line in lines]
poly = Polygon(point)
poly = prep(poly)

acc1, acc2 = 0, 0
for xA,yA in point:
	for xB,yB in point:
		W = abs(xA - xB) + 1
		H = abs(yA - yB) + 1

		area = W * H
		if area > acc1:
			acc1 = area

		rect = box(xA, yA, xB, yB)
		if poly.covers(rect) and area > acc2:
			acc2 = area

print("Part1:", acc1)
print("Part2:", acc2)
