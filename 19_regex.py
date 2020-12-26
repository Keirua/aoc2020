import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/19.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse(data):
	rules = {}
	words = []
	for i,line in enumerate(data):
		if line == "":
			words = data[i+1:]
			return words, rules
		else:
			name, content = line.split(": ")
			rules[name] = content.split(" ")

	return rules

def resolve_token_a(token):
	if token[0] == "\"":
		return token[1] # rules only contain 1 char
	elif token == "|":
		return "|"
	else:
		return "(" + resolve_rule_a(token) + ")"

def resolve_rule_a(rule_number):
	return "".join([resolve_token_a(t) for t in rules[rule_number]])

def resolve_token_b(token):
	if token[0] == "\"":
		return token[1]
	elif token == "|":
		return "|"
	else:
		return "(" + resolve_rule_b(token) + ")"

def resolve_rule_b(rule_number):
	if rule_number == "8":
		# rules["8"] = "42 | 42 8"
		# <=> 42+
		return "(" + resolve_rule_b("42") + ")+"
	elif rule_number == "11":
		# rules["11"] = "42 31 | 42 11 31"
		# <=> 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | …
		# we limit the recursion level, which seems enough to solve the problem
		r42 = "(" + resolve_rule_b("42") + ")"
		r31 = "(" + resolve_rule_b("31") + ")"
		return "|".join(r42*n + r31*n for n in range(1, 5))

	return "".join([resolve_token_b(t) for t in rules[rule_number]])

def part1(words, rules):
	regex = "^" + resolve_rule_a("0") + "$"
	# print(regex)
	return sum([int(re.match(regex, word) is not None) for word in words])

def part2(words, rules):
	regex = "^" + resolve_rule_b("0") + "$"
	# print(regex)
	return sum([int(re.match(regex, word) is not None) for word in words])

words, rules = parse(data)
pp.pprint(rules)

print(part1(words, rules))
print(part2(words, rules))

# assert(match(regex, "ababbb") == True)
# assert(match(regex, "abbbab") == True)
# assert(match(regex, "bababa") == False)
# assert(match(regex, "aaabbb") == False)
# assert(match(regex, "aaaabbb") == False) # may seem to match, but has un unmatched character at the end
