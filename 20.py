import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/20ex.txt', 'r') 
data = [i.strip() for i in file.readlines()]

def parse(data):
	tiles = {}

	for i in range(0, len(data), 12):
		idx = re.findall(r"(\d+)", data[i])[0]
		tile = data[i+1:i+11]
		tiles[idx] = tile

	return tiles


tiles = parse(data)
pp.pprint(tiles)

