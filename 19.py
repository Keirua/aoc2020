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

# CYK algorithm / Cocke–Younger–Kasami algorithm
# https://en.wikipedia.org/wiki/CYK_algorithm
# https://github.com/prscoelho/aoc2020/blob/main/src/day19/day19.rs
def match(rules, word):
	# let the input be a string I consisting of n characters: a1 ... an.
	n = len(word)
	# let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
	r = len(rules)
	# let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
	P = {}
	for i in range(n+1):
		for j in range(n+1):
			for k in range(r+1):
				P[(i,j,k)] = False
	# for each s = 1 to n
	#     for each unit production Rv → as
	#         set P[1,s,v] = true
	for s in range(0,n):
		for v in range(r):
			rule = rules[v]
			if "match" in rule and rule["match"] == word[s]:
				P[(1, s, v)] = True

	# for each l = 2 to n -- Length of span
	#     for each s = 1 to n-l+1 -- Start of span
	#         for each p = 1 to l-1 -- Partition of span
	#             for each production Ra    → Rb Rc
	#                 if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
	for l in range(2, n+1):
		for s in range(0, n-l+2):
			for p in range(1, l):
				for a in range(r):
					rule = rules[a]
					if "rules" in rule and len(rule["rules"]) == 2:
						for subrule in rule["rules"]:
							b = subrule[0]
							c = subrule[1]
							if P[(p, s, b)] == True and P[(l-p, s+p, c)] == True:
								P[(l,s,a)] = True

	# if P[n,1,1] is true then
	#     I is member of language
	# else
	#     I is not member of language
	# pp.pprint(P)
	return P[(n,0,0)]



pp.pprint(rules)
print(words)

assert(match(rules, "ababbb") == True)
assert(match(rules, "abbbab") == True)

assert(match(rules, "bababa") == False)
assert(match(rules, "aaabbb") == False)
assert(match(rules, "aaaabbb") == False) # may seem to match, but has un unmatched character at the end
