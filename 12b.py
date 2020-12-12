import re
file = open('input/12.txt', 'r') 

data = [i.strip() for i in file.readlines()]

x = 0
y = 0

xw = 10
yw = 1

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
	

	if direction in "NSEW":
		xw = xw + (x_nsew[direction] * amount)
		yw = yw + (y_nsew[direction] * amount)

	if direction in 'LR':
		dx = xw
		dy = yw
		if (amount == 90 and direction == "L") or (amount == 270 and direction == "R"):
			xw = -dy
			yw = +dx
		elif amount == 180:
			xw = -dx
			yw = -dy
		elif (amount == 90 and direction == "R") or (amount == 270 and direction == "L"):
			xw = +dy
			yw = -dx
	
	if direction == "F":
		x = x + (xw * amount)
		y = y + (yw * amount)

	print(x, y, xw, yw)

print(abs(x)+abs(y))

