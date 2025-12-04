def max_k_digits(s, k):
    res = []
    start = 0
    n = len(s)

    for remaining in range(k, 0, -1):
        end = n - remaining + 1

        window = s[start:end]
        best_digit = max(window)
        pos = window.index(best_digit) + start

        res.append(best_digit)
        start = pos + 1

    return "".join(res)

def solve(n=2):
    total = 0
    for line in open("input3.txt"):
        digits = line.strip()
        total += int(max_k_digits(digits, n))

    return total

print("Part1:", solve())
print("Part2:", solve(12))
