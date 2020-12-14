import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/13.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse_constraints(l):
	buses = l.split(',')
	indices = list(range(len(buses)))
	return [(int(b), o) for (b, o) in zip(buses, indices) if b != "x"]

all_shuttles = parse_constraints(data[1])

# https://fr.wikipedia.org/wiki/Inverse_modulaire
def modular_inverse(a, n):
	pass

# https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu#Pseudo-code
def extended_euclid_algorithm(a, b):
	r, u, v, rp, up, vp = a, 1, 0, b, 0, 1
	while rp != 0:
		q = r//rp
		r, u, v, rp, up, vp = rp, up, vp, r-q*rp, u - q*up, v-q*vp
	return (r, u, v)

# Finding the solution involves the chinese remainder theorem
# https://math.stackexchange.com/questions/3006823/is-there-an-algorithm-or-formula-to-find-the-alignment-of-multiple-points
def earliest(shuttle_list):
	constraints = parse_constraints(shuttle_list)
	n = 1
	for c in constraints:
		n *= c[0]
	print(extended_euclid_algorithm(23, 120))
	print(constraints)
	print(n)

# print(parse_shuttles(data[1]))
earliest("7,13,x,x,59,x,31,19")

# earliest("7,13,x,x,59,x,31,19") == 1068781
# earliest("17,x,13,19") == 3417
# earliest("67,7,59,61") == 754018
# earliest("67,x,7,59,61") == 779210
# earliest("67,7,x,59,61") == 1261476
# earliest("1789,37,47,1889") == 1202161486


