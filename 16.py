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

def is_valid(value, condition):
	return (value >= condition[0][0] and value <= condition[0][1]) or (value >= condition[1][0] and value <= condition[1][1])

def any_condition_match(v, conditions):
    for c in conditions:
        if is_valid(v, c):
            return True
    return False

def part1(rules, others):
	conditions = rules.values()
	invalid_values = []
	for ticket in others:
		for v in ticket:
			if not any_condition_match(v, conditions):
				invalid_values.append(v)
	return sum(invalid_values)

def filter_valid_tickets(conditions, others):
	valid_tickets = []
	for ticket in others:
		valid = True
		for v in ticket:
			if not any_condition_match(v, conditions):
				valid = False
		if valid:
			valid_tickets.append(ticket)
	return valid_tickets

def part2(rules, mine, others):
	conditions = rules.values()
	valid_tickets = filter_valid_tickets(conditions, others)
	print(valid_tickets)


pp.pprint(lines)
print(rules)
print("mine", mine)
print("others", others)

print(part1(rules, others))
part2(rules, mine, others)