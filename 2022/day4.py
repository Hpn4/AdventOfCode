import re

a = "te.txt"
aa = "input.txt"
file = open(aa, "r")

lines = file.readlines()
acc = 0

for line in lines:
	p = 0
	line = line.strip()

	# Construct an array by casting into integer all the string returned by re.findall
	# re.findall find all the occurences of a specified pattern in a string
	# The r before the ' in the first argument specify to python that we would use regex (regular expression)
	# \d+ is the regex that tells "find numbers"
	# It's the same as r'[0-9]+'
	nmbs = [int(s) for s in re.findall(r'\d+', line)]
	# len(nmbs) = 4
	# pair looks like : nmbs[0]-nmbs[1],nmbs[2]-nmbs[3]

	# In python we can make make two test in one line
	if nmbs[0] <= nmbs[2] <= nmbs[1]:
		p += 1
	elif nmbs[0] <= nmbs[3] <= nmbs[1]:
		p += 1
	elif nmbs[2] <= nmbs[0] <= nmbs[3]:
		p += 1
	elif nmbs[2] <= nmbs[1] <= nmbs[3]:
		p += 1

	acc += p

print(acc)