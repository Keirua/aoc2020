import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/10.txt', 'r') 
adapters = [int(i.strip()) for i in file.readlines()]

builtin_max = max(adapters)+3
adapters.append(builtin_max)

pp.pprint(adapters)
print()
print(builtin_max)

current = 0
nb_1 = 0
nb_3 = 0

adapters.sort()
adapters = adapters[::-1] # reverse
while len(adapters) > 0:
	new_current = adapters.pop()
	diff = new_current - current
	current = new_current
	if diff == 1:
		nb_1+=1
	if diff == 3:
		nb_3+=1

print(nb_1, nb_3, nb_1 * nb_3)
