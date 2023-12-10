lines = open(0, "r").readlines()

# Locate pos of S
startX, startY = 0, 0
for startY in range(len(lines)):
    if 'S' in lines[startY]:
        startX = lines[startY].index('S')
        break
    startY += 1

# Describe how we should move from a given direction
dirs = {'J': {'right': 'up', 'down': 'left'}, 
        '|': {'up': 'up', 'down': 'down'},
        '-': {'right': 'right', 'left': 'left'},
        'L': {'down': 'right', 'left': 'up'},
        '7': {'up': 'left', 'right': 'down'},
        'F': {'up': 'right', 'left': 'down'}}

# Translate direction to deltaX, deltaY
ori = {'up': (0, -1), 'down': (0, 1), 'right': (1, 0), 'left': (-1, 0)}

# First move
def move_next(x, y, o):
    new_ori = dirs[lines[y][x]][o]
    accX, accY = ori[new_ori]

    return x + accX, y + accY, new_ori

def good(x, y, o):
    c = lines[y][x]
    if c in dirs and o in dirs[c]:
        return move_next(x, y, o)

    return None

borders = set()
def get_start():
    borders.add((startX, startY)) # S symbol
    for orientation in ['right', 'left', 'up', 'down']:
        ax, ay = ori[orientation]
        r = good(startX + ax, startY + ay, orientation)

        if r is not None:
            borders.add((startX + ax, startY + ay)) # Point next to S
            borders.add((r[0], r[1])) # After taking this point

            return r

    return None

# Part 1
x, y, o = get_start()
while lines[y][x] != 'S':
    x, y, o = move_next(x, y, o)

    borders.add((x, y))

# Part 2
part2 = 0
for y in range(len(lines)):
    line = lines[y]
    acc = 0
    for x in range(len(line)):
        if (x, y) in borders:
            if line[x] in "|LJS":
                acc += 1
        elif acc % 2 == 1:
            part2 += 1

print("Part1:", len(borders) // 2)
print("Part2:", part2)