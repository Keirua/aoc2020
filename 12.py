import re
file = open('input/12.txt', 'r') 

data = [i.strip() for i in file.readlines()]

x = 0
y = 0

x_nsew = {
	'N':0,
	'S':0,
	'E':1,
	'W':-1,
}

y_nsew = {
	'N':1,
	'S':-1,
	'E':0,
	'W':0,
}

facing_dir = 0
directions = ['E', 'N', 'W', 'S']

for d in data:
	direction = d[0]
	amount = int(d[1:])
	angle_change = amount//90

	if direction in "NSEW":
		x = x + (x_nsew[direction] * amount)
		y = y + (y_nsew[direction] * amount)

	if direction == 'R' :
		facing_dir = (facing_dir + 4 - angle_change) % 4
	if direction == 'L':
		facing_dir = (facing_dir + angle_change) % 4
	if direction == "F":
		x = x + (x_nsew[directions[facing_dir]] * amount)
		y = y + (y_nsew[directions[facing_dir]] * amount)

	print(x, y)

print(abs(x)+abs(y))

