
def find_row_id(row_pass):
	b = 0
	u = 128
	for c in row_pass:
		n_half = (u - b) // 2
		if c == "F":
			u = u - n_half
		else:
			b = b + n_half
	return b

def find_col_id(col_pass):
	b = 0
	u = 8
	for c in col_pass:
		n_half = (u - b) // 2
		if c == "L":
			u = u - n_half
		else:
			b = b + n_half
	return b

def find_seat_id(boarding_pass):
	row = boarding_pass[0:7]
	col = boarding_pass[7:]
	return find_row_id(row) * 8 + find_col_id(col)

def find_pos(boarding_pass):
	row = boarding_pass[0:7]
	col = boarding_pass[7:]
	return (find_row_id(row), find_col_id(col))

print(find_seat_id("FBFBBFFRLR") == 357)
print(find_seat_id("BFFFBBFRRR") == 567)
print(find_seat_id("FFFBBBFRRR") == 119)
print(find_seat_id("BBFFBBFRLL") == 820)


file = open('input/5.txt', 'r') 
data = [i.strip() for i in file.readlines()]
max_id = 0
for p in data:
	nb = find_seat_id(p)
	print(nb, max_id)
	if nb > max_id:
		max_id = nb

print(max_id)


rows = [[0] * 8 for i in range(127)]

for d in data:
	pos = find_pos(d)
	rows[pos[0]][pos[1]] = 1

print(rows)

for y in range(127):
	for x in range(8):
		if rows[y][x] == 0:
			print(y, x, y*8 + x)

