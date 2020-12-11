import re
file = open('input/9.txt', 'r') 
target = 1721308972
# file = open('input/9ex.txt', 'r') 
# target = 127


data = [int(i.strip()) for i in file.readlines()]

def find_pairs(data, offset, preamble):
	l = []
	for i in range(0, preamble):
		for j in range(0, preamble):
			l.append((data[offset-(preamble+1)+i], data[offset-(preamble)+j]))
	return l

def contains_pair_sum(pairs, v):
	found = False
	for p in pairs:
		if v == p[0] + p[1]:
			found = True
			break
	return found


found = False
preamble = 2

def subset(data, offset, preamble):
	s = []
	for i in range(0, preamble):
		s.append(data[offset-(preamble+1)+i])
	return s

while found == False:
	for i in range(0, len(data)-preamble):
		s = data[i:i+preamble]

		if sum(s) == target:
			found = True
			print(min(s) + max(s))
	preamble = preamble + 1
