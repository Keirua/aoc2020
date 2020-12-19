import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/19ex.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse(data):
	rules = {}
	words = []
	for i,line in enumerate(data):
		if line == "":
			words = data[i+1:]
			return words, rules
		else:
			rule = {}
			line = line.split(": ")[1]
			if line.find("\"") > -1:
				rule["match"] = line.replace("\"", "")
			else:
				s = line.split("|")
				ors = list(map(lambda x: list(x.replace(" ", "")), s))
				rule["rules"] = []
				for r in ors:
					rule["rules"].append([int(c) for c in r])
			rules[i] = rule

words, rules = parse(data)



def match(rules, word):
	wpos = 0
	rule_no = 0
	return False


pp.pprint(rules)
print(words)

assert(match(rules, "ababbb") == True)
assert(match(rules, "abbbab") == True)

assert(match(rules, "bababa") == False)
assert(match(rules, "aaabbb") == False)
assert(match(rules, "aaaabbb") == False) # may seem to match, but has un unmatched character at the end
