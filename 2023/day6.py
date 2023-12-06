from math import sqrt

lines = open("input6.txt", "r").readlines()

def get_win(time, dst):
    # Solve equation: (t - x) x > d
    # -x^2 + tx - d > 0
    # delta = t^2 - 4d
    # x0 = t - sqrt(delta) / -2
    # x1 = t + sqrt(delta) / -2
    # x0 - x1 = t - sqrt(delta) / -2 - t - sqrt(delta) / -2
    # x0 - x1 = - 2 sqrt(delta) / -2
    # Keeping rounding
    # x0 - x1 = -2 * floor(-sqrt(delta) / 2) - 1
    return - 2 * (-sqrt(time * time - 4 * dst) // 2) - 1

part1 = 1
time = [int(x) for x in lines[0].split(": ")[1].split()]
dst = [int(x) for x in lines[1].split(": ")[1].split()]

for i in range(len(dst)):
    acc = 0
    for j in range(time[i]):
        if (time[i] - j) * j > dst[i]:
            acc += 1

    part1 *= acc

time = int(lines[0].replace(" ", "").split(":")[1])
dst = int(lines[1].replace(" ", "").split(":")[1])

print("Part1:", part1)
print("Part2:", get_win(time, dst))