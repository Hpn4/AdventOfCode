lines = open("input3.txt", "r").readlines()

height = len(lines)
width = len(lines[0])

part1 = 0
part2 = 0

gear = {}

def char_good(c):
    if c >= '0' and c <= '9':
        return False
    return c != '.' and c != '\n'

def is_gear(c):
    return c == '*'

def is_good2(lines, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            xi = x + i
            yi = y + j

            good = False
            if xi >= 0 and yi >= 0 and xi < width and yi < height:
                good = is_gear(lines[yi][xi])

            if good:
                return xi * width + yi

    return -1

def is_good1(lines, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            xi = x + i
            yi = y + j

            good = False
            if xi >= 0 and yi >= 0 and xi < width and yi < height:
                good = char_good(lines[yi][xi])

            if good:
                return True

    return False

for y in range(height):
    num = ""
    part_num = False
    good = -1

    for x in range(len(lines[y])):
        c = lines[y][x]

        if c >= '0' and c <= '9':
            num += c
            if good == -1:
                good = is_good2(lines, x, y)

            if not part_num:
                part_num = is_good1(lines, x, y)
        else:
            if good >= 0 and len(num) > 0:
                rank = good

                if rank in gear:
                    l = gear[rank]
                    if l[0] == 1:
                        del gear[rank]
                    else:
                        gear[rank] = (1, l[1] * int(num))
                else:
                    gear[rank] = (0, int(num))

            if part_num and len(num) > 0:
                part1 += int(num)

            num = ""
            good = -1
            part_num = False

for value in gear.values():
    if value[0] == 1:
        part2 += value[1]

print("Part1:", part1)
print("Part2:", part2)