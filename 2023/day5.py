import time
l = time.time()
lines = open("input5.txt", "r").readlines()
#lines = open("ex5.txt", "r").readlines()

## PARSING PART
seeds = [int(x) for x in lines[0].split(": ")[1].split()]

parts = []
sub = []
for line in lines[2:]:
    if line == "\n":
        parts.append(sub)
        sub = []
        continue

    if line[0].isdigit():
        sub.append([int(x) for x in line.split()])

## PART 1
def map_part(x, part):
    for p in part:
        dst, src, size = p

        if src <= x < src + size:
            return x - src + dst

    return x

res = []
for seed in seeds:
    s = seed

    for part in parts:
        s = map_part(s, part)

    res.append(s)
part1 = min(res)

## PART2
def map_range(ranges, part):
    mapped = []
    for p in part:
        dst, src, size = p

        i = 0
        while i < len(ranges):
            sr, le = ranges[i]

            # None seeds of the interval match the given map
            if sr >= src + size or sr + le <= src:
                i += 1
                continue

            # Get start and end offset of the mapping
            start = max(sr, src)
            end = min(sr + le, src + size)

            del ranges[i]
            if start - sr > 0:
                ranges.append([sr, start - sr])

            if sr + le - end > 0:
                ranges.append([end, sr + le - end])

            mapped.append([start - src + dst, end - start])

    mapped += ranges

    return mapped

# Range are [src, len] where src + len is not included
ranges = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]

for part in parts:
    ranges = map_range(ranges, part)

part2 = min(ranges, key=lambda v: v[0])

print("Part1:", part1)
print("Part2:", part2[0])
print(time.time() - l)