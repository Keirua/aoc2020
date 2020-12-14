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
DP = {}
def dp(i):
	if i == len(adapters)-1:
		return 1
	if i in DP:
		return DP[i]
	ans = 0
	for j in range(i+1, i+4):
		if j < len(adapters) and (adapters[j] - adapters[i]) <= 3:
			ans += dp(j)
	DP[i] = ans

	return ans


print(dp(0))
