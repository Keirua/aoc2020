import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/17.txt', 'r') 
data = [list(i.strip()) for i in file.readlines()]

ACTIVE = '#'

def neighboor_coordinates(x, y, z, w):
		n = []
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				for dz in [-1, 0, 1]:
					for dw in [-1, 0, 1]:
						if (dx, dy, dz, dw) != (0,0,0, 0):
							n.append((x + dx, y+dy, z + dz, w+dw))
		return n

def bounds(cubes, coord):
	values = [c[coord] for c in cubes]
	return min(values), max(values)

def parse(data):
	on = set()
	
	for y,line in enumerate(data):
		for x,v in enumerate(line):
			if v == ACTIVE:
				on.add((x,y,0,0))
	return on

def print_world(on):
	for c in on:
		print(c)

def step(on):
	bounds_x = bounds(on, 0)
	bounds_y = bounds(on, 1)
	bounds_z = bounds(on, 2)
	bounds_w = bounds(on, 3)
	print(bounds_x, bounds_y, bounds_z, bounds_w)
	print()
	
	next_on = set()
	for x in range(bounds_x[0]-1, bounds_x[1] + 2):
		for y in range(bounds_y[0]-1, bounds_y[1] + 2):
			for z in range(bounds_z[0]-1, bounds_z[1] + 2):	
				for w in range(bounds_w[0]-1, bounds_w[1] + 2):	
					coords = neighboor_coordinates(x, y, z, w)

					nb_active_neighbours = sum([1 if c in on else 0 for c in coords])
					is_active = (x, y, z, w) in on
					if is_active and (nb_active_neighbours == 2 or nb_active_neighbours == 3):
						next_on.add((x, y, z, w))
					if not is_active and (nb_active_neighbours == 3):
						next_on.add((x, y, z, w))
	return next_on

WORLD = parse(data)

print_world(WORLD)
print()
for _ in range(6):
	WORLD = step(WORLD)
	print()
	# print_world(WORLD)
print(len(WORLD))
