file = open('input/3.txt', 'r') 
data = [i.strip() for i in file.readlines()]

h = len(data)
w = len(data[0])

def count_trees(x_offset, y_offset):
	x = 0
	y = 0
	nb_trees = 0
	while y < h:
		if data[y][x] == '#':
			nb_trees += 1
		y += y_offset
		x = (x + x_offset) % w
	return nb_trees

n = 1
for c in [[3, 1], [1,1], [5, 1],[7,1], [1,2]]:
	n = n*count_trees(c[0],c[1])

print(n)
