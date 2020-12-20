import re
import pprint
pp = pprint.PrettyPrinter(indent=4)
from math import sqrt, prod

file = open('input/20.txt', 'r') 
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
	"""
	Extract the 4 borders of a given tile
	"""
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

def rotate_90(original):
    """
    I stole this one here:
    https://stackoverflow.com/a/496056
    """
    # return list(zip(*original[::-1]))
    return list(map(lambda l: "".join(l), zip(*original[::-1])))

def flip_vertical(tile):
	"""
	flip horizontal = read lines in reverse order
	"""
	return tile[::-1]

def generate_all_permutations(tile):
	"""
	Generates all the variations for a tile
	"""
	# Each variant of a tile t can be represented as
	# rot^r(flip^b(t)), where r € [0, 1, 2, 3] and f € [0, 1]
	fv = flip_vertical(tile)
	r90 = rotate_90(tile)
	r180 = rotate_90(r90)
	r90fv = rotate_90(fv)
	r180fv = rotate_90(r90fv)

	permutations = [
		tile,
		fv,
		r90,
		r180,
		rotate_90(r180),
		r90fv,
		r180fv,
		rotate_90(r180fv),
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
	# 	assert(c not in permutations)

	return permutations

def neighbour_coords(x, y):
	"""
	Given coords (x,y), it return the list of the coordinates the valid neighbours
	along with the direction they are in
	"""
	neighbours = {}
	dir = ["west", "north", "east", "south"]
	dx = [-1, 0, 1, 0]
	dy = [0, -1, 0, 1]
	for i in range(len(dx)):
		x2 = x+dx[i]
		y2 = y+dy[i]

		if x2 >= 0 and y2 >=0 and x2 < N and y2 < N:
			neighbours[dir[i]] =  (x2, y2)
	return neighbours

def can_be_neighbour(variant, neighbor_tile, direction):
	"""
	Check if a tile(or a variant) can be neighbour with neighbour_tile in the requested direction
	"""
	bv = borders(variant)
	bn = borders(neighbor_tile)
	if direction == "north": 
		return bv[TOP] == bn[BOTTOM]
	if direction == "south":
		return bv[BOTTOM] == bn[TOP]
	if direction == "east":
		return bv[RIGHT] == bn[LEFT]
	if direction == "west":
		return bv[LEFT] == bn[RIGHT]

	raise("should not happen")


def backtrack():
    coords = [(j, i) for i in range(N) for j in range(N)]
    grid = [[None for _ in range(N)] for _ in range(N)]
    grid_ids = [[None for _ in range(N)] for _ in range(N)]
    unused_ids = list(tiles_with_variations.keys())
    step = 0
    # Backtracking:
    # we add an initial state, with an empty grid and all the tiles to place
    root = {
        'step': step,
        'grid': grid,
        'grid_ids': grid_ids,
        'unused_ids': unused_ids,
    }
    stack = [root]
    while len(stack) > 0:
    	p = stack.pop()
    	step = p["step"]
    	grid = p["grid"]
    	grid_ids = p["grid_ids"]
    	unused_ids = p["unused_ids"]
    	if step == len(coords):
    		return p
    	x,y = coords[step]

    	for tid in unused_ids:
    		for variant in tiles_with_variations[tid]:
    			fits_all_neighbours = True
    			# variant needs to fit in every valid neighbouring cell that is a tile
    			neighbouring_cell_coords = neighbour_coords(x, y)
    			for _, (dir, coord) in enumerate(neighbouring_cell_coords.items()):

    				neighbor_tile = grid[coord[1]][coord[0]]
    				# If there is a tile already, we want to ensure this variant can be neighbour with
    				# the existing neighbour cell, in the given direction
    				if not neighbor_tile is None:
    					# 
    					if not can_be_neighbour(variant, neighbor_tile, dir):
    						fits_all_neighbours = False
    						break
    			# If this variant cannot fit in every direction, we move on to another variant
    			# Otherwise, we add this new state to the stack
    			if not fits_all_neighbours:
    				continue
    			else:
    				next_grid = [row[:] for row in grid]
    				next_grid_ids = [row[:] for row in grid_ids]
    				next_grid[y][x] = variant
    				next_grid_ids[y][x] = tid
    				next_unused_ids = unused_ids[:]
    				next_unused_ids.remove(tid)
    				new_state = {
    					"step": step + 1,
    					"grid": next_grid,
    					"grid_ids": next_grid_ids,
    					"unused_ids": next_unused_ids
    				}
    				stack.append(new_state)

tiles = parse(data)
N = int(sqrt(len(tiles.keys())))

tiles_with_variations = {}
for t_id in tiles.keys():
	all_perms = generate_all_permutations(tiles[t_id])
	tiles_with_variations[t_id] = all_perms
pp.pprint(tiles_with_variations)

p = backtrack()
g = p["grid"]
pp.pprint(g)
for y, l in enumerate(g):
	for x, c in enumerate(l):
		print(x, y, g[y][x])

def p1(grid_ids):
	l = len(grid_ids)
	corner_cells =  [
		grid_ids[0][0],
		grid_ids[-1][0],
		grid_ids[-1][-1],
		grid_ids[0][-1],
	]
	return prod(corner_cells)
print(p1(p["grid_ids"]))
