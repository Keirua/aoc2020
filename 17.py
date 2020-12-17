import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/17ex.txt', 'r') 
data = [list(i.strip()) for i in file.readlines()]

ACTIVE = '#'
INACTIVE = '.'

class Cube:
	def __init__(self, x, y, z, state):
		self.x = x
		self.y = y
		self.z = z
		self.state = state

	def __repr__(self):
		return "{} {} {} {}".format(self.x, self.y, self.z, self.state)

	def neighboor_coordinates(self):
		n = []
		d = [-1, 0, 1]
		for dx in range(d):
			for dy in range(d):
				for dz in range(d):
					if dx != 0 and dy != 0 and dz != 0:
						n.append((dx, dy, dy))
		return n

def parse_world(data):
	world = []
	z = 0
	for y,line in enumerate(data):
		for x,v in enumerate(line):
			c = Cube(x,y,z,v)
			world.append(c)
	return world

WORLD = parse_world(data)

for c in WORLD:
	print(c)
