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

tiles = parse(data)
pp.pprint(tiles)

print(borders(tiles[2311]))
