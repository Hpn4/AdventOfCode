import re
from collections import deque

# Get all the integers in the line
def getInt(line):
	return [int(x) for x in re.findall(r'-?\d+', line)]

# Read the file 'file' and return a list of all the lines stripped()
def readAndStrip(file):
	return list(map(lambda l: l.strip(), open(a).readlines()))

# Sum elements of l in intervals [start, end[
def sumOf(l, start, end):
	acc = 0
	for i in range(start, end):
		acc += l[i]

	return acc

def productOf(l, start, end):
	acc = 1
	for i in range(start, end):
		acc *= l[i]

	return acc


# Simple queue class with 3 operations, isempty, enqueue and dequeue
class Queue:

	def __init__(self):
		self.q = deque()

	def isempty(self):
		return len(self.q) == 0

	def enqueue(self, x):
		self.q.append(x)

	def dequeue(self):
		return self.q.popleft()

# Simple Stack class
class Stack:

	def __init__(self):
		self.q = deque()

	def isempty(self):
		return len(self.q) == 0

	def push(self, x):
		self.q.append(x)

	def peek(self):
		return self.q[-1]

	def pop(self):
		return self.q.pop()