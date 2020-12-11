import re
file = open('input/9.txt', 'r') 
preamble = 25
# file = open('input/9ex.txt', 'r') 
# preamble = 5

data = [int(i.strip()) for i in file.readlines()]

def find_pairs(data, offset, preamble):
	l = []
	for i in range(0, preamble):
		for j in range(0, preamble):
			# if i != j:
			l.append((data[offset-(preamble+1)+i], data[offset-(preamble)+j]))
	return l

def contains_pair_sum(pairs, v):
	found = False
	for p in pairs:
		if v == p[0] + p[1]:
			found = True
			break
	return found

for i in range(preamble+1, len(data)):
	pairs = find_pairs(data, i, preamble)
	found = contains_pair_sum(pairs, data[i])
	if found == False:
		print(data[i])
