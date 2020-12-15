import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

input = "5,2,8,16,18,0,1"
input = "0,3,6"

def parse(input):
	return [int(i) for i in input.split(",")]


def nth(l, n):
	OCC = {}
	pos = len(l)
	for i, x in enumerate(l):
		OCC[x] = i+1
	while(len(l) < n):
		last_value = l[-1]
		if l.count(last_value) == 1:
			l.append(0)
		else:
			diff = pos - OCC[last_value]
			l.append(diff)

		OCC[last_value] = pos
		pos = pos+1
	return l[-1]


assert(nth(parse("1,3,2"), 2020) == 1)
assert(nth(parse("2,1,3"), 2020) == 10)
# print(nth(parse("0,3,6"), 10))

input = "5,2,8,16,18,0,1"
target = 30000000
data = parse(input)
print(data)
print(nth(data, 30000))
