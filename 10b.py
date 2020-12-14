import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/10.txt', 'r') 
adapters = [int(i.strip()) for i in file.readlines()]

builtin_max = max(adapters)+3
adapters.append(builtin_max)

current = 0

adapters.sort()

stack = [0]
nb_valid = 0
while len(stack) > 0:
	current = stack.pop()
	valid_plugs = list(filter(lambda k: current < k <= current + 3, adapters))
	for v in valid_plugs:
		if v == builtin_max:
			nb_valid = nb_valid + 1
		else:
			stack.append(v)

print(nb_valid)

