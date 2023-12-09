lines = open(0, "r").readlines()

part1 = 0
part2 = 0

parts = [[int(x) for x in line.split()] for line in lines]
for part in parts:
    pred = [(part[0], part[-1])]
    n = part

    while not all([x == 0 for x in n]):
        n = [n[j] - n[j - 1] for j in range(1, len(n))]

        pred.append((n[0], n[-1]))

    num1, num2 = 0,0
    for i in range(len(pred) - 1, -1, -1):
        start, end = pred[i]
        num1 += end
        num2 = start - num2

    part1 += num1
    part2 += num2

print("Part1:", part1)
print("Part2:", part2)