lines = open(0, "r").readlines()

def getv(valu, x):
    return len(valu) - 1 - valu.index(x)

def gettype(part1, valu, x):
    H = [0] * len(valu)

    # Build histogram of cards
    for c in x:
        H[getv(valu, c)] += 1

    # For part2 The Joker 'J' can be any card so we put it aside
    if part1:
        jc = 0
    else:
        jc = H[getv(valu, 'J')]
        H[getv(valu, 'J')] = 0

    H = sorted(H, reverse=True)
    if H[0] + jc == 5:
        return 7

    if H[0] + jc == 4:
        return 6

    if (H[0] + jc == 3 and H[1] == 2) or (H[0] == 3 and H[1] + jc == 2):
        return 5

    if H[0] + jc == 3:
        return 4

    if (H[0] + jc == 2 and H[1] == 2) or (H[0] == 2 and H[1] + jc == 2):
        return 3

    if H[0] + jc == 2:
        return 2

    if H[0] == 1 and H[1] == 1 and H[2] == 1 and H[3] == 1 and (H[4] == 1 or jc == 1):
        return 1

    return 0

def sort_hands(part1=True):
    if part1:
        valu = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    else:
        valu = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    acc = 0
    hands = []
    for line in lines:
        hand, num = line[:-1].split()
        rank = gettype(part1, valu, hand)

        nw = [chr(ord('A') + getv(valu, h)) for h in hand]

        hands.append((rank, nw, int(num)))

    hands = sorted(hands, key=lambda x: (x[0], x[1]))

    return sum((i + 1) * hand[2] for i,hand in enumerate(hands))

print("Part1:", sort_hands(True))
print("Part2:", sort_hands(False))