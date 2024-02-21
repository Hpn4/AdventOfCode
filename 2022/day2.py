
file = open("input.txt", "r")

lines = file.readlines()

acc = 0
for line in lines:
	line = line.strip()

	first = line[0]
	second = line[2]

	point = 0

	if first == 'A': # Rock
		if second == 'Y': # Draw
			point += 3 + 1
		elif second == 'Z': # Win
			point += 6 + 2
		elif second == 'X': # Loss
			point += 3
	elif first == 'B': #
		if second == 'Y': # Draw paper
			point += 3
			point += 2
		elif second == 'Z': # Win
			point += 6 + 3
		elif second == 'X': # Loss
			point += 1
	elif first == 'C': # Scissors
		if second == 'Y': # Draw
			point += 3 + 3
		elif second == 'Z': # Win
			point += 6 + 1
		elif second == 'X': # Loss
			point += 2

	acc += point

print(acc)