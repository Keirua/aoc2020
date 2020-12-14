import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/10.txt', 'r') 
adapters = [int(i.strip()) for i in file.readlines()]

builtin_max = max(adapters)+3
adapters.append(builtin_max)
adapters.append(0)

adapters.sort()

# This comment helped to understand the dynamic solution
# https://www.reddit.com/r/adventofcode/comments/kacdbl/2020_day_10c_part_2_no_clue_how_to_begin/gf9lzhd/
paths = {}
for c in adapters:
	paths[c] = 0
paths[0] = 1

for current in adapters:
	plugs = [current + 1, current + 2, current + 3]
	for v in plugs:
		if v in adapters:
			paths[v] = paths[v] + paths[current]
	pp.pprint(paths)

print(paths[builtin_max])
