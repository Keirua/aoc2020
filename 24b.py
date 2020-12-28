import re
file = open('input/24.txt', 'r') 
import pprint
pp = pprint.PrettyPrinter(indent=4)
from collections import defaultdict, deque

data = [i.strip() for i in file.readlines()]

#https://www.redblobgames.com/grids/hexagons/#neighbors-axial
offsets = {
	"w" : [-1,  0],
	"e" : [ 1,  0],
	"nw": [ 0, -1],
	"ne": [ 1, -1],
	"sw": [-1, +1],
	"se": [ 0,  1],
}

def compute_movements(directions):
	# https://stackoverflow.com/questions/6661169/finding-adjacent-neighbors-on-a-hexagonal-grid
	x,y = 0,0
	for d in directions:
		dx, dy = offsets[d]
		x += dx
		y += dy
	return (x, y)

def neighbours(x, y):
	n = set()
	for dx, dy in offsets.values():
		n.add((x+dx, y+dy))
	return n

def neighbours_of(list_of_cells):
	n = set()
	for x,y in list_of_cells:
		curr_n = neighbours(x, y)
		n = n | curr_n
	return n

def neighbour_count(x, y, black):
	return len(neighbours(x, y) & black)

def generate_initial_floor():
	black = set()

	for line in data:
		directions = re.findall("e|w|ne|nw|se|sw", line)
		pos = compute_movements(directions)
		if pos in black:
			black.remove(pos)
		else:
			black.add(pos)
	return black

black = generate_initial_floor()

def step(black):
	new_black = black.copy()

	for x,y in black:
		c = neighbour_count(x,y, black)
		if c == 0 or c >= 2:
			new_black.remove((x,y))
	white = neighbours_of(black)
	for x,y in white:
		c = neighbour_count(x,y, black)
		if c == 2:
			new_black.add((x,y))

	return new_black

print(len(data))
print(len(black))
print(black)
for i in range(1, 100+1):
	black = step(black)
	print("day {} - {} ".format(i, len(black)))