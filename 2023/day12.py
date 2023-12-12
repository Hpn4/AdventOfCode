lines = open(0, "r").readlines()

# memo retain already calculated combination
# line: the #.?. sequence. infos: list of int
# pos: index in line, infospos: index in infos
# count: number of hashtag seen
def getcount(memo, line, infos, pos, count, infospos):
    key = (pos, count, infospos)

    if key in memo: # Avoid redo the same thing
        return memo[key]

    if pos == len(line):
        ret = 1 if infospos == len(infos) else 0

    elif line[pos] == '#': # Move pos and increment counter of hashtag
        ret = getcount(memo, line, infos, pos + 1, count + 1, infospos)

    elif line[pos] == '.' or infospos == len(infos):
        if infospos < len(infos) and count == infos[infospos]:
            ret = getcount(memo, line, infos, pos + 1, 0, infospos + 1)
        elif count == 0: # Two .. succesivly
            ret = getcount(memo, line, infos, pos + 1, 0, infospos)
        else:
            ret = 0 # Don't match
    else:
        # Behave like hashtag
        ret = getcount(memo, line, infos, pos + 1, count + 1, infospos)

        # Behave like dot
        if count == infos[infospos]:
            ret += getcount(memo, line, infos, pos + 1, 0, infospos + 1)
        elif count == 0:
            ret += getcount(memo, line, infos, pos + 1, 0, infospos)

    memo[key] = ret
    return ret

part1 = 0
part2 = 0
for line in lines:
    line = line[:-1]

    payload, info = line.split()
    infos = [int(x) for x in info.split(",")]

    part1 += getcount({}, payload + '.', infos, 0, 0, 0)

    infos = infos * 5
    payload = (payload + '?') * 4 + payload + '.'

    part2 += getcount({}, payload, infos, 0, 0, 0)

print("Part 1:", part1)
print("Part 2:", part2)