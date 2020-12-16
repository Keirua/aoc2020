import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/16ex.txt', 'r') 
lines = [i.strip() for i in file.readlines()]

def parse_numbers(line, s=","):
	return [int(i) for i in line.split(s)]

def parse_rule(line):
	rules_split = line.split(": ")
	name = rules_split[0]
	conditions_split = rules_split[1].split(" or ")
	conditions = [
		parse_numbers(conditions_split[0], "-"),
		parse_numbers(conditions_split[1], "-")
	]
	return (name, conditions)
	
def parse(lines):
	step = "rules"
	rules = {}
	mine = None
	others = []
	for i in range(len(lines)):
		line = lines[i]
		if step == "rules":

			if line == "":
				step = "mine"
			else:
				name, conditions = parse_rule(line)
				rules[name] = conditions
				

		elif step == "mine":
			if line == "":
				step = "others"
			elif line.find("ticket") == -1:
				mine = parse_numbers(line)
		elif step == "others" and line.find("ticket") == -1:
			others.append(parse_numbers(line))
	return rules, mine, others

rules, mine, others = parse(lines)

pp.pprint(lines)
print(rules)
print("mine", mine)
print("others", others)
