import re
file = open('input/24ex.txt', 'r') 
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

dots = []

for line in data:
	directions = re.findall("e|w|ne|nw|se|sw", line)
	pos = compute_movements(directions)
	if pos in dots:
		print("remove {}".format(pos))
		dots.remove(pos)
	else:
		print("add {}".format(pos))
		dots.append(pos)

print(len(data))
# 198 = too low
print(len(dots))
