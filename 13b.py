import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/13.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse_shuttles(l):
	buses = l.split(',')
	offsets = list(range(len(buses)))
	return [(int(b), o) for (b, o) in zip(buses, offsets) if b != "x"]

all_shuttles = parse_shuttles(data[1])

# Finding the solution involves the chinese remainder theorem
# https://math.stackexchange.com/questions/3006823/is-there-an-algorithm-or-formula-to-find-the-alignment-of-multiple-points
def earliest(timestamp):
	pass

# print(parse_shuttles(data[1]))
print(parse_shuttles("7,13,x,x,59,x,31,19"))

# earliest("7,13,x,x,59,x,31,19") == 1068781
# earliest("17,x,13,19") == 3417
# earliest("67,7,59,61") == 754018
# earliest("67,x,7,59,61") == 779210
# earliest("67,7,x,59,61") == 1261476
# earliest("1789,37,47,1889") == 1202161486


