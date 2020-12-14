import re
import pprint
from collections import deque, defaultdict
pp = pprint.PrettyPrinter(indent=4)

file = open('input/7.txt', 'r') 
data = [i.strip() for i in file.readlines()]

# In part 1, we need to keep track of which bags have other bags as containers
# In part 2, we need to keep track of which bags (and how many) each bag contains

# our graph: the vertices are bags, and the edges are:
#  - part1: which bags might contain us
#  - part2: which bags and how many we contain
PARENTS = defaultdict(list)  # parents[x] = the bags that contain x
CONTENTS = defaultdict(list) # contents[x] = the bags contained by x

def parse(data):
	for line in data:
		sep = line.split(" contain ")
		containees = sep[1].split(", ")
		container = sep[0][:-5] # [:-5] removes " bags"

		containees = list(map(lambda x: x.replace(" bags", "").replace(" bag", "").rstrip("."), containees))
		if containees[0] == "no other":
			continue

		rebags = list(map(lambda x: re.findall("(\\d+) (.*)", x), containees))
		for result in rebags:
			result = result[0]
			bag = result[1]
			n = int(result[0])
			PARENTS[bag].append(container)
			CONTENTS[container].append((bag, n))

parse(data)

# Solution that involves a queue and a set, which are faster than lists
def bag_count(target):
	"""
	Starting from target, how many bags can we reach by following the edges ?
	BFS: breadth first search.
	BFS solves this problem by visiting every vertex reachable from a given vertex.
	"""
	SEEN = set()
	Q = deque([target])
	while Q:
		curr = Q.popleft()
		if curr in SEEN:
			continue
		SEEN.add(curr)
		for p in PARENTS[curr]:
			Q.append(p)

	return len(SEEN)-1

def size(target):
	"""
	DFS: depth first search
	DFS visit all the children before visiting the 
	"""
	ans = 1
	for (y, n) in CONTENTS[target]:
		ans += n * size(y)
	return ans

target = "shiny gold"
print(bag_count(target))
print(size(target) -1)
