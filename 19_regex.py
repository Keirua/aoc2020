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
			rules[name] = content.strip().split(" ")

	return rules

def resolve_token(token):
	if token.startswith("\""):
		return token[1]
	elif token == "|":
		return "|"
	else:
		return "(" + resolve_rule(token) + ")"

def resolve_rule(rule_number):
	return "".join([resolve_token(t) for t in rules[rule_number]])

def part1(words, rules):
	regex = "^" + resolve_rule("0") + "$"
	print(regex)
	return sum([1 for word in words if re.match(regex, word)])

words, rules = parse(data)
pp.pprint(rules)

print(part1(words, rules))

# assert(match(regex, "ababbb") == True)
# assert(match(regex, "abbbab") == True)
# assert(match(regex, "bababa") == False)
# assert(match(regex, "aaabbb") == False)
# assert(match(regex, "aaaabbb") == False) # may seem to match, but has un unmatched character at the end
