import re
import pprint
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

def has_shiny(bags):
	nb_shiny = 0
	visited = []
	has_parents = ["shiny gold"]
	while len(has_parents) > 0:
		curr_child = has_parents.pop()
		for c in bags.keys():
			if curr_child in bags[c].keys() and c not in visited:
				nb_shiny = nb_shiny + 1
				visited.append(c)
				has_parents.append(c)
		# print(has_parents)

	return nb_shiny

n = has_shiny(bags)
print(n)


