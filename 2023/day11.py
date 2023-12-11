from itertools import combinations

lines = open(0, "r").readlines()

galaxies = []
empties = []

# Find galaxies and empty lines
for y in range(len(lines)):
    line = lines[y].strip()
    empty = True

    for x in range(len(line)):
        if line[x] == '#':
            galaxies.append((x, y))
            empty = False

    if empty:
        empties.append((-1, y))

# Find empty column
for x in range(len(lines[0])):
    empty = True

    for y in range(len(lines) - 1):
        if lines[y][x] == '#':
            empty = False

    if empty:
        empties.append((x, -1))

def count_beetween(s, e):
    x1,y1 = s
    x2,y2 = e

    exp = 0
    for x,y in empties:
        if x == -1 and (y1 <= y <= y2 or y2 <= y <= y1):
            exp += 1

        if y == -1 and (x1 <= x <= x2 or x2 <= x <= x1):
            exp += 1

    return exp

part1 = 0
part2 = 0
for (s,e) in combinations(galaxies, 2):
    exp = count_beetween(s, e)

    p1 = exp * 2 - exp # Twie as big
    p2 = exp * 1000000 - exp # One million bigger

    # Shortest path when move left,right,up,down = Manhattan distance
    d = abs(e[0] - s[0]) + abs(e[1] - s[1])

    # Manhattan distance + expension
    part1 += d + p1
    part2 += d + p2

print("Part1:", part1)
print("Part2:", part2)