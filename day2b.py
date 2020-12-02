file = open('input/2.txt', 'r') 
data = [i.strip().split(' ') for i in file.readlines()]

count = 0

for p in data:
	numbers = [int(i) for i in p[0].split('-')]
	password = p[2]
	letter = p[1].strip(':')

	print(numbers, password, letter)
	if (password[numbers[0]-1] == letter) ^ (password[numbers[1]-1] == letter):
		count += 1


print(count)
# print(data)