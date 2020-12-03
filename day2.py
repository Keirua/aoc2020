file = open('input/2.txt', 'r') 
data = [i.strip().split(' ') for i in file.readlines()]

rules = []

count = 0
for p in data:
	numbers = [int(i) for i in p[0].split('-')]
	password = p[2]
	letter = p[1].strip(':')
	nb = password.count(letter)

	print(numbers, password, letter)
	if nb >= numbers[0] and nb <= numbers[1]:
		count += 1

print(count)
# print(data)