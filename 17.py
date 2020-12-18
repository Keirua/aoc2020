import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/17ex.txt', 'r') 
data = [list(i.strip()) for i in file.readlines()]

ACTIVE = '#'

def neighboor_coordinates(x, y, z):
		n = []
		d = [-1, 0, 1]
		for dx in d:
			for dy in d:
				for dz in d:
					if (dx, dy, dz) != (0,0,0):
						n.append((x + dx, y+dy, z + dz))
		return n

def bounds(cubes, coord):
	values = [c[coord] for c in cubes]
	return min(values), max(values)

def active_count(on, cubes):
	nb = 0
	for c in cubes:
		if c in on:
			nb += 1
	return nb

class World:
	def __init__(self):
		self.on = set()

	def parse(self, data):
		self.on = set()
		
		for y,line in enumerate(data):
			for x,v in enumerate(line):
				if v == ACTIVE:
					self.on.add((x,y,0))
		return self.on

	def print(self):
		for c in self.on:
			print(c)

	def step(self):
		bounds_x = bounds(self.on, 0)
		bounds_y = bounds(self.on, 1)
		bounds_z = bounds(self.on, 2)
		
		next_on = set()
		for x in range(bounds_x[0]-1, bounds_x[1] + 2):
			for y in range(bounds_y[0]-1, bounds_y[1] + 2):
				for z in range(bounds_z[0]-1, bounds_z[1] + 2):		
					coords = neighboor_coordinates(x, y, z)
					nb_active_neighbours = active_count(self.on, coords)
					is_active = (active_count(self.on, [(x,y,z)]) == 1)

					if is_active and (nb_active_neighbours == 2 or nb_active_neighbours == 3):
						pass
					if not is_active and (nb_active_neighbours == 3):
						next_on.add((x, y, z))
		self.on = next_on

WORLD = World()
WORLD.parse(data)

WORLD.print()
print()
WORLD.step()
print()
WORLD.print()

# for i in range(6):
# 	print(i)
# 	WORLD = WORLD.step()
# 	WORLD.print()