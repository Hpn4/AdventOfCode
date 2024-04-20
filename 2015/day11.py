inp = "cqjxjnds"

def valid(s):
    if "i" in s or "o" in s or "l" in s:
        return False

    good = False
    j = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            good = True
            j = i
            break

    if not good:
        return False
    good = False
    for i in range(j + 2, len(s) - 1):
        if s[i] == s[i + 1]:
            good = True
            break

    if not good:
        return False

    for i in range(len(s) - 2):
        c1 = ord(s[i])
        c2 = ord(s[i + 1])
        c3 = ord(s[i + 2])

        if c1 + 1 == c2 and c1 + 2 == c3:
            return True

    return False

def incr(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'z':
            s[i] = 'a'
        else:
            s[i] = chr(ord(s[i]) + 1)
            break

def next(inp):
    inp = [c for c in inp]
    incr(inp)

    while not valid(inp):
        incr(inp)

    a = ""
    for c in inp:
        a += c

    return a

part1 = next(inp)
part2 = next(part1)

print("Part1:", part1)
print("Part2:", part2)