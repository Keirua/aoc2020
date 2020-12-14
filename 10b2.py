import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/10.txt', 'r') 
adapters = [int(i.strip()) for i in file.readlines()]

builtin_max = max(adapters)+3
adapters.append(builtin_max)
adapters.append(0)

adapters.sort()
# Rewrote a solution in order to get dynamic programming
# https://www.youtube.com/watch?v=cE88K2kFZn0

# dp(i) = the number of ways to reach the end given we currently are at adapter i
def dp_v1(i):
	"""
	A first solution in exponential time (O(fib(n)) ?)
	"""
	# From the end, there is only one path
	if i == len(adapters)-1:
		return 1
	ans = 0
	# one way to get from i to the end is to go from all the valid j to the end, that is to say from dp(j)
	# dp(i) = \sum_{valid j} dp(j)
	for j in range(i+1, i+4):
		if j < len(adapters) and (adapters[j] - adapters[i]) <= 3:
			ans += dp(j)

	return ans

DP = {}
def dp_v2(i):
	"""
	Another version, in linear time O(n)
	Time complexity in a memoized DP problem = 
	  - how many times you call dp (= what is the size of the input)
	  - how many operations you do in the non-recursive part (here, the for loop)
	memory complexity = O(n)
	"""
	if i == len(adapters)-1:
		return 1
	# once you are at a known step, you dont care how you got there
	if i in DP:
		return DP[i]
	ans = 0

	for j in range(i+1, i+4):
		if j < len(adapters) and (adapters[j] - adapters[i]) <= 3:
			ans += dp(j)
	# memoization for later use
	DP[i] = ans

	return ans


print(dp_v2(0))
