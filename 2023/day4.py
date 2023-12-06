lines = open("input4.txt", "r").readlines()

part1 = 0
copy = [1] * len(lines)

for i in range(len(lines)):
    left, right = lines[i].split(": ")[1].split('|')

    win = set(left.split())
    acc = sum([x in win for x in right.split()])

    if acc > 0:
        part1 += 2**(acc - 1)

    for j in range(acc):
        copy[j + i + 1] += copy[i]

print("Part1:", part1)
print("Part2:", sum(copy))