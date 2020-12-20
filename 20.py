import re
import pprint
pp = pprint.PrettyPrinter(indent=4)
from math import sqrt, prod

TOP, BOTTOM, LEFT, RIGHT = 0, 1, 2, 3

BORDER_CACHE = {}
NEIGHBOUR_CACHE = {}

def parse(data):
    tiles = {}

    for i in range(0, len(data), 12):
        idx = int(re.findall(r"(\d+)", data[i])[0])
        tile = data[i+1:i+11]
        tiles[idx] = tile

    return tiles

def borders(tile):
    """
    Extract the 4 borders of a given tile
    """
    if id(tile) in BORDER_CACHE:
        return BORDER_CACHE[id(tile)]

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
    BORDER_CACHE[id(tile)] = b
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
    Each variant of a tile t can be represented as
    rotate90^r(flip_vertical^b(t)), where r € [0, 1, 2, 3] and f € [0, 1]
    """
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

    return permutations

def neighbour_coords(x, y):
    """
    Given coords (x,y), it return the list of the coordinates the valid neighbours
    along with the direction they are in
    """
    if (x, y) in NEIGHBOUR_CACHE:
        return NEIGHBOUR_CACHE[(x, y)]
    neighbours = {}
    dir = [LEFT, BOTTOM, RIGHT, TOP]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(len(dx)):
        x2 = x+dx[i]
        y2 = y+dy[i]

        if x2 >= 0 and y2 >=0 and x2 < N and y2 < N:
            neighbours[dir[i]] =  (x2, y2)
    NEIGHBOUR_CACHE[(x,y)] = neighbours
    return neighbours

def can_be_neighbour(variant, neighbor_tile, direction):
    """
    Check if a tile(or a variant) can be neighbour with neighbour_tile in the requested direction
    """
    bv = borders(variant)
    bn = borders(neighbor_tile)
    if direction == TOP: 
        return bv[TOP] == bn[BOTTOM]
    if direction == BOTTOM:
        return bv[BOTTOM] == bn[TOP]
    if direction == RIGHT:
        return bv[RIGHT] == bn[LEFT]
    if direction == LEFT:
        return bv[LEFT] == bn[RIGHT]

    raise("should not happen")


def variant_can_fit(variant, grid, x, y):
    fits_all_neighbours = True
    # variant needs to fit in every valid neighbouring cell that has already been placed
    neighbouring_cell_coords = neighbour_coords(x, y)
    for _, (dir, coord) in enumerate(neighbouring_cell_coords.items()):
        if (coord[1],coord[0]) in grid:
            # If there is a tile already, we want to ensure this variant can be neighbour with
            # the existing neighbour cell, in the given direction
            if not can_be_neighbour(variant, grid[(coord[1],coord[0])], dir):
                return False
    return True

def backtrack():
    coords = [(j, i) for i in range(N) for j in range(N)]
    grid = {}
    grid_ids = {}
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
        step, grid, grid_ids, unused_ids = p["step"], p["grid"], p["grid_ids"], p["unused_ids"]

        x,y = coords[step]

        # We go through all the variants of all the remaining tiles, and check if they fit in position x,y
        # This is only possible if they match the neighbour's borders
        for tid in unused_ids:
            for variant in tiles_with_variations[tid]:
                # If this variant cannot fit in every direction, we move on to another variant
                # Otherwise, we add this new state to the stack
                if variant_can_fit(variant, grid, x, y):
                    next_grid = grid.copy()
                    next_grid_ids = grid_ids.copy()
                    next_grid[(y,x)] = variant
                    next_grid_ids[(y,x)] = tid
                    next_unused_ids = unused_ids[:]
                    next_unused_ids.remove(tid)
                    new_state = {
                        "step": step + 1,
                        "grid": next_grid,
                        "grid_ids": next_grid_ids,
                        "unused_ids": next_unused_ids
                    }
                    # If we have used all the ids, we are done
                    if len(next_unused_ids) == 0:
                        return new_state
                    stack.append(new_state)


file = open('input/20ex.txt', 'r') 
data = [i.strip() for i in file.readlines()]

tiles = parse(data)
N = int(sqrt(len(tiles.keys())))

tiles_with_variations = {}
for t_id in tiles.keys():
    all_perms = generate_all_permutations(tiles[t_id])
    tiles_with_variations[t_id] = all_perms

p = backtrack()
g = p["grid"]
pp.pprint(g)
for y, l in enumerate(g):
    for x, c in enumerate(l):
        if (y,x) in g:
            print(x, y, g[(y,x)])

def p1(grid_ids):
    """
    Computes the product of all the corner cells
    """
    l = len(grid_ids)
    corner_cells =  [
        grid_ids[(0,0)],
        grid_ids[(N-1,0)],
        grid_ids[(N-1,N-1)],
        grid_ids[(0,N-1)],
    ]
    return prod(corner_cells)


def monster_pattern_offsets():
    """
    Converts the monster pattern into a list of the offsets where the monster must appear
    """
    monster_pattern = r"""..................#.
#....##....##....###
.#..#..#..#..#..#...   
"""
    positions = []
    lines = monster_pattern.split("\n")
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#":
                positions.append((x, y))
    return positions

def p2(p):
    g = p["grid"]
    key = list(tiles.keys())[0]
    tile_w = len(tiles[key])
    print(tile_w)
    image = [["."] * (N+1) * tile_w] * (N+1) * tile_w
    # For all the tiles in the grid
    for y, l in enumerate(g):
        for x, c in enumerate(l):
            # if (y,x) in g:
            #     print(x, y, g[(y,x)], c)

            if (y,x) in g:
                y0 = (tile_w-2) * y
                x0 = (tile_w-2) * x
                variant = g[(y, x)]
                # Plot the tile in the image
                for yv in range(1, tile_w-1):
                    for xv in range(1, tile_w-1):
                        # print(x0, y0, xv, yv)
                        image[y0 + yv][x0 + xv] = variant[yv][xv]

    # Display the image
    for line in image:
        print("".join(line))
    # pp.pprint(image)

# print(p1(p["grid_ids"]))
# p2(p)
print(monster_pattern_offsets())