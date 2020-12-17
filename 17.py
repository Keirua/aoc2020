import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/17ex.txt', 'r') 
data = [list(i.strip()) for i in file.readlines()]

ACTIVE = '#'
INACTIVE = '.'

def neighboor_coordinates(x, y, z):
		n = []
		d = [-1, 0, 1]
		for dx in d:
			for dy in d:
				for dz in d:
					if (dx, dy, dz) != (0,0,0):
						n.append((x + dx, y+dy, z + dz))
		return n

class Cube:
	def __init__(self, x, y, z, state):
		self.x = x
		self.y = y
		self.z = z
		self.state = state

	def __repr__(self):
		return "{} {} {} {}".format(self.x, self.y, self.z, self.state)

class World:
	def __init__(self):
		self.cubes = []
		pass

	def parse(self, data):
		self.cubes = []
		self.x_bounds = [0,len(data)]
		self.y_bounds = [0,len(data[0])]
		self.z_bounds = [0,0]
		z = 0
		for y,line in enumerate(data):
			for x,v in enumerate(line):
				c = Cube(x,y,z,v)
				self.cubes.append(c)
				print(c)
		print(len(self.cubes))
		return self.cubes

	def print(self):
		print(len(self.cubes))
		for c in self.cubes:
			if c is not None:
				print(c)

def find_cubes_states(world, cubes):
	v = []
	for w in world:
		for c in cubes:
			if w.x == c[0] and w.y == c[1] and w.z == c[2]:
				v.append(w.state)
	return v

WORLD = World()
WORLD.parse(data)

# def step(WORLD):
# 	new_world = []
# 	for c in WORLD:
# 		n = c.neighboor_coordinates()
# 		states = find_cubes_states(WORLD, n)
# 		print(states)

# 		new_state = c.state
# 		active_count = states.count(ACTIVE)
# 		if c.state == ACTIVE and (active_count == 2 or active_count == 3):
# 			new_state = INACTIVE
# 		if c.state == INACTIVE and (active_count == 3):
# 			new_state = ACTIVE
# 		new_world.append(Cube(c.x, c.y, c.z, new_state))
# 	return new_world

WORLD.print()
# for i in range(6):
# 	print(i)
# 	print_world(WORLD)
# 	WORLD = step(WORLD)
# 	print()