import re
import pprint
from collections import defaultdict
pp = pprint.PrettyPrinter(indent=4)

def parse(input):
	return [int(i) for i in input.split(",")]

class Latestpair(object):
	def __init__(self):
		self.mini = None
		self.maxi = None

	def add(self, x):
		self.mini = self.maxi
		self.maxi = x

	def diff(self):
		return self.maxi - self.mini

	def __repr__(self):
		return "{},{}".format(self.maxi, self.mini)

def latestpair():
	return Latestpair()

def nth(l, n):
	pos = len(l)
	COUNTS = defaultdict(int)
	OCC = defaultdict(latestpair)
	for i, x in enumerate(l):
		COUNTS[x] = 1
		OCC[x].add(i)

	last_value = l[-1]

	while(pos < n):
		if COUNTS[last_value] == 1:
			last_value = 0
		else:
			last_value = OCC[last_value].diff()

		COUNTS[last_value] += 1
		OCC[last_value].add(pos)

		pos = pos + 1

	return last_value

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

print(nth(parse(input), target))
