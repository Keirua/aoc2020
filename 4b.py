import re
file = open('input/4.txt', 'r') 
data = [i.strip() for i in file.readlines()]

# cid optionnal in part 1
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

current_passport = ""
nb_valid = 0

def check_passport(passport):
	fields = passport[1:].split(" ")
	content = {}
	for field in fields:
		key = field.split(":")
		content[key[0]] = key[1]

	for r in required_fields:
		if r not in content.keys():
			return False

	if not (1920 <= int(content["byr"]) <= 2002):
		# print(fields, "byr", content["byr"])
		return False
	if not (2010 <= int(content["iyr"]) <= 2020):
		# print(fields, "iyr", content["iyr"])
		return False
	if not (2020 <= int(content["eyr"]) <= 2030):
		# print(fields, "eyr", content["eyr"])
		return False

	height = int(content["hgt"][0:-2])
	height_unit = content["hgt"][-2:]
	if height_unit == "cm":
		if not (150 <= height <= 193):
			# print(fields, "hgt", content["hgt"])
			return False
	elif height_unit == "in":
		if not (59 <= height <= 76):
			# print(fields, "hgt", content["hgt"])
			return False
	else:
		return False

	if not (re.match(r'\#[0-9a-f]{6}', content["hcl"])):
		# print(fields, "hcl", content["hcl"])
		return False
	if not (content["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
		# print(fields, "ecl", content["ecl"])
		return False
	if not (re.match(r'[0-9]{9}', content["pid"])):
		# print(fields, "pid", content["pid"])
		return False

	fields.sort()
	print(fields)

	return True

passports = []

for line in data:
	if line == "":
		passports.append(current_passport)
		current_passport = ""
	else:
		current_passport = current_passport + " " + line
# special case for the last 
if current_passport != "":
	passports.append(current_passport)


for passport in passports:
	if check_passport(passport):
		nb_valid += 1

print(nb_valid)
