# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
# while there are tokens to be read:
#     read a token.
#     if the token is a number, then:
#         push it to the output queue.
#     else if the token is an operator then:
#         while ((there is an operator at the top of the operator stack)
#               and ((the operator at the top of the operator stack has greater precedence)
#                   or (the operator at the top of the operator stack has equal precedence and the token is left associative))
#               and (the operator at the top of the operator stack is not a left parenthesis)):
#             pop operators form the operator stack onto the output queue.
#         push it onto the operator stack.
#     else if the token is a left parenthesis (i.e. "("), then:
#         push it onto the operator stack.
#     else if the token is a right parenthesis (i.e. ")"), then:
#         while the operator at the top of the operator stack is not a left parenthesis:
#             pop the operator from the operator stack onto the output queue.
#         /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
#         if there is a left parenthesis at the top of the operator stack, then:
#             pop the operator from the operator stack and discard it
#         if there is a function token at the top of the operator stack, then:
#             pop the function from the operator stack onto the output queue.
# /* After while loop, if operator stack not null, pop everything to output queue */
# if there are no more tokens to read then:
#     while there are still operator tokens on the stack:
#         /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
#         pop the operator from the operator stack onto the output queue.

# Check implem with
# https://rosettacode.org/wiki/Parsing/RPN/Ruby

import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/18.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse_infix_to_rpn(tokens):
	"""
	Converts from infix to RPN with the shunting yard algorithm
	"""
	output = []
	operators = []
	for t in tokens.replace(" ", ""):
		if t in "0123456789":
			output.append(int(t[0]))
		if t == "+" or t == "*":
			if len(operators) > 0:
				o = operators[-1]
				if o != "(":
					output.append(o)
					operators.pop()
			operators.append(t)
		if t == "(":
			operators.append("(")
		if t == ")":
			while len(operators) > 0:
				o = operators.pop()
				if o == "(":
					break
				else:
					output.append(o)
		# print(t, operators, output)

	while len(operators) > 0:
		output.append(operators.pop())

	return output

def eval_rpn(tokens):
	"""
	Evaluates a RPN expression and returns the result
	"""
	stk = []
	operations = {
		"+": lambda a, b: a+b,
		"*": lambda a, b: a*b,
	}
	for t in tokens:
		if isinstance(t, int):
			stk.append(t)
		else:
			a = stk.pop()
			b = stk.pop()
			stk.append(operations[t](a, b))
	assert(len(stk) == 1)
	return stk[0]


def p1(expr):
	return eval_rpn(parse_infix_to_rpn(expr))

sample_tokens = [
	("2 * 3 + (4 * 5)", 26),
	("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
	("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
	("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
]
for s,e in sample_tokens:
	# print(s, e)
	parsed = parse_infix_to_rpn(s)
	# print(parsed)
	# print(eval_rpn(parsed))
	assert(eval_rpn(parsed) == e)

print(sum(map(p1, data)))
# print(sum(map(p2, data)))