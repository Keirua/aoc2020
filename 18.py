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

import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/18.txt', 'r') 
expressions = [list(i.strip()) for i in file.readlines()]

def parse(tokens):
	output = []
	operators = []
	for t in tokens:
		if t == " ":
			continue
		if t in "0123456789":
			output.append(int(t[0]))
		if t == "+" or t == "*":
			while len(operators) > 0:
				o = operators.pop()
				if o != "(":
					output.append(o)
				else:
					break
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

	while len(operators) > 0:
		output.append(operators.pop())

	return output

tokens = "2 * 3 + (4 * 5)"
print(tokens)
# for tokens in expressions:
print(parse(tokens))
