import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/20ex.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse(data):
	tiles = {}

	for i in range(0, len(data), 12):
		idx = int(re.findall(r"(\d+)", data[i])[0])
		tile = data[i+1:i+11]
		tiles[idx] = tile

	return tiles

TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3

def borders(tile):
	l = len(tile)
	b = [
		# top
		tile[0],
		# bottom
		tile[l-1],
		# left
		"".join([tile[j][0] for j in range(l)]),
		# right
		"".join([tile[j][l-1] for j in range(l)])
	]
	return b



def possible_neighbours(tile, tiles):
	neighbours = {
		"north": [],
		"south": [],
		"east": [],
		"west": []
	}
	b = borders(tile)
	for _, (k,v) in enumerate(tiles.items()):
		bn = borders(v)
		if bn[BOTTOM] == b[TOP]:
			neighbours["north"].append(k)
		if bn[TOP] == b[BOTTOM]:
			neighbours["south"].append(k)
		if bn[LEFT] == b[RIGHT]:
			neighbours["east"].append(k)
		if bn[RIGHT] == b[LEFT]:
			neighbours["west"].append(k)
	return neighbours


tiles = parse(data)
pp.pprint(tiles)

print(borders(tiles[2311]))
neighbours = {}
for t_id in tiles.keys():
 	n = possible_neighbours(tiles[t_id], tiles)
 	neighbours[t_id] = n

pp.pprint(neighbours)