file = open('input/3.txt', 'r') 
data = [i.strip() for i in file.readlines()]

h = len(data)
w = len(data[0])
x = 0
y = 0

nb_trees = 0
print(w)
while y < h:
	if data[y][x] == '#':
		nb_trees += 1
	y += 1
	x = (x + 3) % w
print(nb_trees)
# print(data)