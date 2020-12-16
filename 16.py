import re
import pprint
from functools import reduce
pp = pprint.PrettyPrinter(indent=4)

file = open('input/16.txt', 'r') 
lines = [i.strip() for i in file.readlines()]

def parse_numbers(line, s=","):
	return [int(i) for i in line.split(s)]

def parse_rule(line):
	rules_split = line.split(": ")
	name = rules_split[0]
	conditions_split = rules_split[1].split(" or ")
	conditions = list(map(lambda c: parse_numbers(c, "-"), conditions_split))
	return (name, conditions)
	
def parse(lines):
	# Parsing through a basic state machine.
	# State goes from "rules" to "mine" then "other".
	# Transition happen when an empty line is found
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
	return any([value >= c[0] and value <= c[1] for c in condition])

def any_condition_match(v, conditions):
    return any([is_valid(v, c) for c in conditions])

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

def condition_match_every_tickets(condition, p, tickets):
	return all([is_valid(ticket[p], condition) for ticket in tickets])

def extract_possible_positions(rules, valid_tickets):
	possible_positions = {}
	for k in rules.keys():
		possible_positions[k] = []
	for p in range(len(valid_tickets[0])):
		for k in rules.keys():
			r = rules[k]
			if condition_match_every_tickets(r, p, valid_tickets):
				possible_positions[k].append(p)
	return possible_positions

def extract_positions_from(possible_positions):
	# find the final positions through constraint propagation
	positions = {}
	categories = possible_positions.keys()
	for i in range(len(categories)):
		remain1 = list(filter(lambda k: len(possible_positions[k]) == 1, categories))
		for r in remain1:
			actual_position = possible_positions[r][0]
			positions[r] = actual_position
			for c in categories:
				if actual_position in possible_positions[c]:
					possible_positions[c].remove(actual_position)
	return positions

def part2(rules, mine, others):
	conditions = rules.values()
	valid_tickets = filter_valid_tickets(conditions, others)
	valid_tickets.append(mine)
	
	possible_positions = extract_possible_positions(rules, valid_tickets)
	positions = extract_positions_from(possible_positions)

	pp.pprint(positions)

	# Computes the product of the departure values on the owner ticket 
	departure_positions = filter(lambda k: k.startswith("departure"), positions.keys())
	total = reduce(lambda x, y: mine[positions[y]]*x, departure_positions, 1)

	return total

print(part1(rules, others))
print(part2(rules, mine, others))