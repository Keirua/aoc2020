import re
import pprint
from collections import deque
pp = pprint.PrettyPrinter(indent=4)

file = open('input/7.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse(data):
	bags = {}
	for line in data:
		sep = line.split(" contain ")
		containees = sep[1].split(", ")
		container = sep[0][:-5]
		if container not in bags:
			bags[container] = {}
		containees = list(map(lambda x: x.replace(" bags", "").replace(" bag", "").rstrip("."), containees))
		if containees[0] == "no other":
			continue
		else:
			rebags = list(map(lambda x: re.findall("(\\d+) (.*)", x), containees))
			for result in rebags:
				result = result[0]
				bags[container][result[1]] = int(result[0])
	return bags

bags = parse(data)
pp.pprint(bags)

# Solution that involves a queue and a set, which are faster than lists
def bag_count(bags, target):
	nb_shiny = 0
	SEEN = set()
	Q = deque([target])
	while Q:
		curr_child = Q.popleft()
		for c in bags.keys():
			if curr_child in bags[c].keys() and c not in SEEN:
				nb_shiny = nb_shiny + 1
				SEEN.add(c)
				Q.append(c)

	return len(SEEN)-1

print(bag_count(bags, "shiny gold"))
