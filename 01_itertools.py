file = open('input/1.txt', 'r') 
data = [int(i.strip()) for i in file.readlines()]
from itertools import combinations
from math import prod

def answer(data, n):
	return ([prod(s) for s in combinations(data, n) if sum(s) == 2020])

print(answer(data, 2))
print(answer(data, 3))