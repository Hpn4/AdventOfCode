from math import lcm

lines = open(0, "r").readlines()

# Get instructions and trunc it from the file
instr = lines[0].strip()
lines = lines[2:]

# Parsing store in dict current: (left, right)
part = {}
names = []
for line in lines:
    line = line[:-1].replace(" ", "")

    name, sec = line.split('=')

    part[name] = sec[1:-1].split(",")

    # For part2
    if name.endswith('A'):
        names.append(name)

# Return the number of step to reach a node
# that end up with stop in his name starting from name
def follow(name, stop):
    acc = 0
    i = 0

    while not name.endswith(stop):
        if i >= len(instr):
            i = 0

        name = part[name][instr[i] == 'R']
        i += 1
        acc += 1

    return acc

print("Part1:", follow("AAA", "ZZZ"))

# For each, calculate how many steps to reach an end
# Then compute the lcm of all of these indices
def ppcm():
    l = [follow(name, "Z") for name in names]
    i = l[0]
    for j in range(1, len(l)):
        i = lcm(i, l[j])
        
    return i

print("Part2:", ppcm())