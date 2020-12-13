import re
file = open('input/11.txt', 'r') 

data = [list(i.strip()) for i in file.readlines()]

W = len(data[0])
H = len(data)

def neighbors(data, x, y):
	n = []
	dx = [-1, 0, 1,  0,   -1,1,1,-1]
	dy = [ 0, 1, 0, -1,   -1,1,-1,1]
	for i in range(8):
		nx = x+dx[i]
		ny = y+dy[i]
		if nx >= 0 and nx < W and ny >=0 and ny < H:
			n.append(data[ny][nx])

	return n

def evolve(data):
	nb_changes = 0
	new_data = []
	for y in range(H):
		line = []
		for x in range(W):
			v = data[y][x]
			n = neighbors(data, x, y)
			if data[y][x] == "L" and n.count("#") == 0:
				v = "#"
				nb_changes = nb_changes + 1
			elif data[y][x] == "#" and n.count("#") >= 4:
				v = "L"
				nb_changes = nb_changes + 1
			line.append(v)
		new_data.append(line)

	return nb_changes, new_data

def draw_state(data):
	for l in data:
		print("".join(l))

draw_state(data)

def occupied(data):
	o = 0
	for line in data:
		o = o+line.count("#")
	return o

new_data = data
nb_changes = None
while nb_changes is None or nb_changes > 0:
	nb_changes, new_data = evolve(new_data)
	# print()
	# draw_state(new_data)

# print(new_data)
print(occupied(new_data))