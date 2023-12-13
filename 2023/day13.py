lines = open(0, "r").read()

parts = lines.split('\n\n')

part1 = 0
part2 = 0
for part in parts:
    p = part.split('\n')
    w = len(p[0])
    h = len(p)

    # Find row sym
    for y in range(h - 1):
        d = 0
        for j in range(h):
            up = y - j
            down = y + j + 1
            if 0 <= up < down < h:
                d += sum(p[up][x] != p[down][x] for x in range(w))

        if d == 1:
            part2 += 100 * (y + 1)
        if d == 0:
            part1 += 100 * (y + 1)

    # Find col sym
    for x in range(w - 1):
        d = 0
        for j in range(w):
            left = x - j
            right = x + j + 1

            if 0 <= left < right < w:
                d += sum(p[y][left] != p[y][right] for y in range(h))

        if d == 1:
            part2 += x + 1
        if d == 0:
            part1 += x + 1

print("Part1:", part1)
print("Part2:", part2)