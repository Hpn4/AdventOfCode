import sys

lines = open(sys.argv[1], "r").readlines()
lines = lines[2:] # Skip part and labels

def strToSec(str):
    if '>' in str:
        return 24 * 3600
    h, m, s = str.split(':')

    return int(h) * 3600 + int(m) * 60 + int(s)

def secToStr(sec):
    h = sec // 3600
    sec = sec % 3600
    m = sec // 60
    sec = sec % 60

    return f"{int(h)}:{int(m)}:{int(sec)}"

stats = [0 for _ in range(6)]
for line in lines:
    line = line.replace("  ", " ")
    day, time1, rank1, score1, time2, rank2, score2 = line.split()

    stats[0] += strToSec(time1)
    stats[1] += int(rank1)
    stats[2] += int(score1)

    stats[3] += strToSec(time2)
    stats[4] += int(rank2)
    stats[5] += int(score2)

for i in range(2):
    print(f"========== PART {i + 1} ==========")
    print(f"Average time for part{i + 1}:", secToStr(stats[i * 3 + 0] / 25))
    print(f"Average rank for part{i + 1}:", stats[i * 3 + 1] / 25)
    print(f"Average score for part{i + 1}:", stats[i * 3 + 2] / 25)
