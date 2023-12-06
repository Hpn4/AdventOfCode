lines = open("input1.txt", "r").readlines()

def equ(s, i, st):
    if len(st) + i >= len(s):
        return False

    for j in range(len(st)):
        if s[i + j] != st[j]:
            return False

    return True

def getN(line, i):
    if line[i] >= '1' and line[i] <= '9':
        return line[i]

    num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for j in range(len(num)):
        if line[i:].startswith(num[j]):
            return str(j + 1)

    return None

acc = 0
m = []
for line in lines:
    l = ""

    i = 0
    while i < len(line):
        num = getN(line, i)
        if num is None:
            i += 1
        else:
            l = num
            break

    i = len(line) - 1
    while i >= 0:
        num = getN(line, i)
        if num is None:
            i -= 1
        else:
            l += num
            break

    acc += int("" + l[0] + l[-1])


print(acc)