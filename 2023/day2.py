lines = open("input2.txt", "r").readlines()

def prod(l):
    acc = 1
    for ent in l:
        acc *= ent

    return acc

part1 = 0
part2 = 0
i = 1
for line in lines:
    line = line.split(": ")[1]

    ha = {"green": 0, "red": 0, "blue": 0}
    for game in line.split(";"):
        for w in game.split(","):
            a,b = w.split()

            if int(a) > ha[b]:
                ha[b] = int(a)

    if ha['red'] <= 12 and ha['green'] <= 13 and ha['blue'] <= 14:
        part1 += i

    part2 += prod(ha.values())

    i += 1

print("Part1:", part1)
print("Part2:", part2)