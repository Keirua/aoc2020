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

def rotate_90(original):
    """
    I stole this one here:
    https://stackoverflow.com/a/496056
    """
    # return list(zip(*original[::-1]))
    return list(map(lambda l: "".join(l), zip(*original[::-1])))

def rotate_m90(original):
    return list(map(lambda l: "".join(l), list(zip(*original))[::-1]))

def rotate_m180(original):
    return rotate_m90(rotate_m90(original))

def rotate_m270(original):
    return rotate_m90(rotate_m90(rotate_m90(original)))

def rotate_180(original):
	return rotate_90(rotate_90(original))

def rotate_270(original):
	return rotate_90(rotate_90(rotate_90(original)))

def flip_horizontal(tile):
	"""
	flip horizontal = read columns in reverse order
	"""
	l = len(tile)
	out = [list("."* len(tile)) for i in range(l)]
	for y in range(l):
		for x in range(l):
			out[y][x] = tile[y][l-1-x]
	for y in range(l):
			out[y] = "".join(out[y])
	return out

def flip_vertical(tile):
	"""
	flip horizontal = read lines in reverse order
	"""
	return tile[::-1]

tiles = parse(data)
pp.pprint(tiles)

# print("original tile")
# pp.pprint(tiles[2311])
# print("rotate_90")
# pp.pprint(rotate_90(tiles[2311]))
# print("rotate_180")
# pp.pprint(rotate_180(tiles[2311]))
# print("rotate_270")
# pp.pprint(rotate_270(tiles[2311]))
# print("flip_vertical")
# pp.pprint(flip_vertical(tiles[2311]))
# print("flip_horizontal")
# pp.pprint(flip_horizontal(tiles[2311]))

def generate_all_permutations(tile):
	# Each variant of a tile t can be represented as
	# rot^r(flip^b(t)), where r € [0, 1, 2, 3] and f € [0, 1]
	permutations = [
		tile,
		flip_vertical(tile),
		rotate_90(tile),
		rotate_180(tile),
		rotate_270(tile),
		rotate_90(flip_vertical(tile)),
		rotate_180(flip_vertical(tile)),
		rotate_270(flip_vertical(tile)),
	]

	# I was not so sure of that, so a bunch of checks happened
	# others = [
	# 	flip_horizontal(tile),
	# 	rotate_90(flip_horizontal(tile)),
	# 	rotate_180(flip_horizontal(tile)),
	# 	rotate_270(flip_horizontal(tile)),
	# 	rotate_270(flip_horizontal(flip_vertical(tile))),
	# 	rotate_180(flip_horizontal(flip_vertical(tile))),
	# 	rotate_90(flip_horizontal(flip_vertical(tile))),
	# 	rotate_m90(flip_horizontal(tile)),
	# 	rotate_m180(flip_horizontal(tile)),
	# 	rotate_m270(flip_horizontal(tile)),
	# 	rotate_m270(flip_horizontal(flip_vertical(tile))),
	# 	rotate_m180(flip_horizontal(flip_vertical(tile))),
	# 	rotate_m90(flip_horizontal(flip_vertical(tile)))
	# ]
	# for i,c in enumerate(others):
	# 	if c not in permutations:
	# 		print("missing {}".format(i))

	return permutations

print("borders of the original tile")
print(borders(tiles[2311]))
pp.pprint(generate_all_permutations(tiles[2311]))

print()
neighbours = {}
for t_id in tiles.keys():
 	n = possible_neighbours(tiles[t_id], tiles)
 	neighbours[t_id] = n

pp.pprint(neighbours)

possible_tiles = {}
for t_id in tiles.keys():
	all_perms = generate_all_permutations(tiles[t_id])
	for i,p in enumerate(all_perms):
		possible_tiles[(t_id, i)] = p
pp.pprint(possible_tiles)		