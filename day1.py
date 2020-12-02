file = open('input/1.txt', 'r') 
data = [int(i.strip()) for i in file.readlines()]

for d in data:
	other = 2020 - d
	if other in data:
		print(d * other)

print(data)