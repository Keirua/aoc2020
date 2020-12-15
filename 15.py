import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

input = "5,2,8,16,18,0,1"

def parse(input):
	return [int(i) for i in input.split(",")]

def nth(l, n):
	pos = len(l)
	while(pos < n):
		last_value = l[-1]
		if l.count(last_value) == 1:
			l.append(0)
		else:
			occurences = [i for i, x in enumerate(l) if x == last_value]
			l.append(occurences[-1] - occurences[-2])
		pos = pos + 1
	return l[-1]

assert(nth(parse("1,3,2"), 2020) == 1)
assert(nth(parse("2,1,3"), 2020) == 10)
assert(nth(parse("1,3,2"), 2020) == 1)
assert(nth(parse("2,1,3"), 2020) == 10)
assert(nth(parse("1,2,3"), 2020) == 27)
assert(nth(parse("2,3,1"), 2020) == 78)
assert(nth(parse("3,2,1"), 2020) == 438)
assert(nth(parse("3,1,2"), 2020) == 1836)

data = parse(input)
print(data)
print(nth(data, 2020))
