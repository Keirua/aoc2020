import re
import pprint
from collections import defaultdict
pp = pprint.PrettyPrinter(indent=4)

input = "5,2,8,16,18,0,1"

def parse(input):
	return [int(i) for i in input.split(",")]

def nth(l, n):
	pos = len(l)
	COUNTS = defaultdict(int)
	OCC = defaultdict(list)
	for i, x in enumerate(l):
		COUNTS[x] = 1
		OCC[x].append(i)

	last_value = l[-1]
	while(pos < n):
		if COUNTS[last_value] == 1:
			l.append(0)
			last_value = 0
			COUNTS[0] += 1
			OCC[0].append(pos)
		else:
			# occurences = [i for i, x in enumerate(l) if x == last_value]
			# print(last_value, OCC[last_value])
			last_value = OCC[last_value][-1] - OCC[last_value][-2]
			OCC[last_value].append(pos)

			# l.append(last_value)
			COUNTS[last_value] += 1
		# print(l)
		pos = pos + 1

	return last_value

assert(nth(parse("0,3,6"), 10) == 0)
# assert(nth(parse("1,3,2"), 2020) == 1)
# assert(nth(parse("2,1,3"), 2020) == 10)
# assert(nth(parse("1,3,2"), 2020) == 1)
# assert(nth(parse("2,1,3"), 2020) == 10)
# assert(nth(parse("1,2,3"), 2020) == 27)
# assert(nth(parse("2,3,1"), 2020) == 78)
# assert(nth(parse("3,2,1"), 2020) == 438)
# assert(nth(parse("3,1,2"), 2020) == 1836)

# input = "5,2,8,16,18,0,1"
# target = 30000000
# target = 2020
# data = parse(input)
# print(data)
# print(nth(data, target))
