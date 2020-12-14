import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/13.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse_constraints(l):
	buses = l.split(',')
	indices = list(range(len(buses)))
	return [(int(b) - o, int(b)) for (b, o) in zip(buses, indices) if b != "x"]

# https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu#Pseudo-code
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, x, y = egcd(b % a, a)
		return (g, y - (b//a) * x, x)

# Finding the solution involves the chinese remainder theorem
# https://math.stackexchange.com/questions/3006823/is-there-an-algorithm-or-formula-to-find-the-alignment-of-multiple-points
# https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_restes_chinois#Algorithme
# I should have looked at a solution from rosetta code: 
# https://rosettacode.org/wiki/Chinese_remainder_theorem
def earliest(shuttle_list):
	constraints = parse_constraints(shuttle_list)
	n_hat = 1

	shortest = 0
	for c in constraints:
		n_hat *= c[1]
	for r,m in constraints:
		p = n_hat // m
		step = r * ((egcd(p, m)[1] % m + m)%m) * p

		shortest = shortest + step
	return shortest % n_hat


assert(earliest("7,13,x,x,59,x,31,19") == 1068781)
assert(earliest("17,x,13,19") == 3417)
assert(earliest("67,7,59,61") == 754018)
assert(earliest("67,x,7,59,61") == 779210)
assert(earliest("67,7,x,59,61") == 1261476)
assert(earliest("1789,37,47,1889") == 1202161486)

print(earliest(data[1]))
