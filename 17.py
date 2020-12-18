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

def find_cubes_states(world, cubes):
	v = []
	for w in world:
		for c in cubes:
			if w.x == c[0] and w.y == c[1] and w.z == c[2]:
				v.append(w.state)
	return v

def find_curr_cube_state(world, cubes):
	for w in world:
		for c in cubes:
			if w.x == c[0] and w.y == c[1] and w.z == c[2]:
				return (w.state)
	return INACTIVE

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
		self.x_bounds = [0,0]
		self.y_bounds = [0,0]
		self.z_cycle = 0

		pass

	def parse(self, data):
		self.cubes = []
		self.x_bounds = [0,len(data)]
		self.y_bounds = [0,len(data[0])]
		self.z_cycle = 0
		for y,line in enumerate(data):
			for x,v in enumerate(line):
				c = Cube(x,y,self.z_cycle,v)
				self.cubes.append(c)
		return self.cubes

	def print(self):
		print(self.x_bounds, self.y_bounds, self.z_cycle)
		for c in self.cubes:
			if c is not None:
				print(c)

	def step(self):
		new_world = World()
		new_world.x_bounds = [self.x_bounds[0]-1, self.x_bounds[1] + 1]
		new_world.y_bounds = [self.y_bounds[0]-1, self.y_bounds[1] + 1]
		new_world.z_cycle += 1
		print(new_world.x_bounds, new_world.y_bounds, new_world.z_cycle)

		for x in range(new_world.x_bounds[0], new_world.x_bounds[1] + 1):
			for y in range(new_world.y_bounds[0], new_world.y_bounds[1] + 1):
				for z in range(-new_world.z_cycle, new_world.z_cycle + 1):
					coords = neighboor_coordinates(x, y, z)
					curr_cube_state = find_curr_cube_state(self.cubes, coords)
					states = find_cubes_states(self.cubes, coords)

					new_state = INACTIVE
					active_count = states.count(ACTIVE)
					if curr_cube_state == ACTIVE and (active_count == 2 or active_count == 3):
						new_state = INACTIVE
					if curr_cube_state == INACTIVE and (active_count == 3):
						new_state = ACTIVE
					new_world.cubes.append(Cube(x, y, z, new_state))
		return new_world

WORLD = World()
WORLD.parse(data)

# WORLD.print()
WORLD = WORLD.step()
print()
WORLD.print()

# for i in range(6):
# 	print(i)
# 	WORLD = WORLD.step()
# 	WORLD.print()