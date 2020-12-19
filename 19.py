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
	return False
	# curr_rule_no = 0
	# curr_rule_idx = 0
	# parent_rule = rules[curr_rule_no]
	# child_rules = [ rules[p[curr_rule_idx]] for p in parent_rule["rules"] ]
	# if(len(child_rules) == 1) and "match" in child_rules[0].keys():
	# 	if child_rules[0]["match"] == word[wpos]:
	# 		print("match for {}".format(child_rules[0]["match"]))
	# return False


pp.pprint(rules)
print(words)

assert(match(rules, "ababbb") == True)
assert(match(rules, "abbbab") == True)

assert(match(rules, "bababa") == False)
assert(match(rules, "aaabbb") == False)
assert(match(rules, "aaaabbb") == False) # may seem to match, but has un unmatched character at the end
