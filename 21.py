import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/21ex.txt', 'r') 
data = [i.strip().replace(")", "") for i in file.readlines()]
def parse(data):
	allergens = []
	for line in data:
		t = " (contains "
		offset = line.find(" (contains ")
		cipher = line[0:offset].split(" ")
		plaintext = line[offset+len(t):].split(", ")
		allergens.append((cipher, plaintext))
	return allergens

print(parse(data))