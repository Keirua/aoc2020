file = open('input/4.txt', 'r') 
data = [i.strip() for i in file.readlines()]

# cid optionnal in part 1
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

current_passport = ""
nb_valid = 0

def check(passport):
	fields = passport[1:].split(" ")
	content = {}
	for field in fields:
		key = field.split(":")
		content[key[0]] = key[1]
	for r in required_fields:
		if r not in content.keys():
			return False
	return True

for line in data:
	if line == "":
		print(current_passport[1:])
		if check(current_passport):
			nb_valid += 1
		current_passport = ""
	else:
		current_passport = current_passport + " " + line

print(nb_valid)
