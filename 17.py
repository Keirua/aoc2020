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
	return sum([c in on for c in cubes])

def parse(data):
	on = set()
	
	for y,line in enumerate(data):
		for x,v in enumerate(line):
			if v == ACTIVE:
				on.add((x,y,0))
	return on

def print_world(on):
	for c in on:
		print(c)

def step(on):
	bounds_x = bounds(on, 0)
	bounds_y = bounds(on, 1)
	bounds_z = bounds(on, 2)
	print(bounds_x, bounds_y, bounds_z)
	print()
	
	next_on = set()
	# for x in range(bounds_x[0]-1, bounds_x[1] + 2):
	# 	for y in range(bounds_y[0]-1, bounds_y[1] + 2):
	# 		for z in range(bounds_z[0]-1, bounds_z[1] + 2):	
	for x in range(-15, 15):
		for y in range(-15, 15):
			for z in range(-15, 15):
				coords = neighboor_coordinates(x, y, z)

				nb_active_neighbours = active_count(on, coords)
				is_active = (active_count(on, [(x,y,z)]) == 1)

				if not is_active and (nb_active_neighbours == 3):
					next_on.add((x, y, z))
	return next_on

WORLD = parse(data)

print_world(WORLD)
print()
for _ in range(6):
	WORLD = step(WORLD)
	print()
	# print_world(WORLD)
print(len(WORLD))
