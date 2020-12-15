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
	for i, x in enumerate(l):
		COUNTS[x] = 1
	# print(COUNTS)

	while(pos < n):
		last_value = l[-1]
		# print(l)
		# print(last_value)
		if COUNTS[last_value] == 1:
			# print("first time !")
			l.append(0)
			COUNTS[0] += 1
		else:
			occurences = [i for i, x in enumerate(l) if x == last_value]
			# print(last_value, occurences, COUNTS)
			l.append(occurences[-1] - occurences[-2])
			COUNTS[occurences[-1] - occurences[-2]] += 1
		pos = pos + 1
	# 	print()
	# print(l)
	return l[-1]

assert(nth(parse("0,3,6"), 10) == 0)
assert(nth(parse("1,3,2"), 2020) == 1)
assert(nth(parse("2,1,3"), 2020) == 10)
assert(nth(parse("1,3,2"), 2020) == 1)
assert(nth(parse("2,1,3"), 2020) == 10)
assert(nth(parse("1,2,3"), 2020) == 27)
assert(nth(parse("2,3,1"), 2020) == 78)
assert(nth(parse("3,2,1"), 2020) == 438)
assert(nth(parse("3,1,2"), 2020) == 1836)

input = "5,2,8,16,18,0,1"
target = 30000000
target = 2020
data = parse(input)
print(data)
print(nth(data, target))
