import re
import pprint
pp = pprint.PrettyPrinter(indent=4)
from collections import defaultdict

file = open('input/21ex.txt', 'r') 
data = [i.strip().replace(")", "") for i in file.readlines()]
def parse(data):
	allergens = []
	for line in data:
		t = " (contains "
		offset = line.find(" (contains ")
		cipher = set(line[0:offset].split(" "))
		plaintext = set(line[offset+len(t):].split(", "))
		allergens.append((cipher, plaintext))
	return allergens


def extract_possible_words(allergens):
	possible_words = {}
	all_cipher_ingredients = set()
	for cipher,plaintext in allergens:
		all_cipher_ingredients = all_cipher_ingredients.union(plaintext)

		for p in plaintext:
			if p not in possible_words:
				possible_words[p] = set(cipher)
			else:
				possible_words[p] = possible_words[p].intersection(cipher)
	return possible_words, all_cipher_ingredients


allergens = parse(data)
possible_words = extract_possible_words(allergens)
print()
pp.pprint(possible_words)