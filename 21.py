import re
import pprint
pp = pprint.PrettyPrinter(indent=4)
from collections import defaultdict

file = open('input/21.txt', 'r') 
data = [i.strip().replace(")", "") for i in file.readlines()]
def parse(data):
    recipes = []
    for line in data:
        t = " (contains "
        offset = line.find(" (contains ")
        cipher = set(line[0:offset].split(" "))
        plaintext = set(line[offset+len(t):].split(", "))
        recipes.append((cipher, plaintext))
    return recipes

def extract_possible_words(recipes):
    possible_words = {}
    all_cipher_ingredients = set()
    for cipher,plaintext in recipes:
        all_cipher_ingredients = all_cipher_ingredients.union(cipher)

        for p in plaintext:
            if p not in possible_words:
                possible_words[p] = set(cipher)
            else:
                possible_words[p] = possible_words[p].intersection(cipher)
    return possible_words, all_cipher_ingredients

def extract_allergens(possible_words):
    allergens_cipher = set()
    for _,(p,c) in enumerate(possible_words.items()):
        allergens_cipher = allergens_cipher.union(c)
    return allergens_cipher

recipes = parse(data)
possible_words, all_cipher_ingredients = extract_possible_words(recipes)

allergens_cipher = extract_allergens(possible_words)
safe_cipher = all_cipher_ingredients.difference(allergens_cipher)
nb_non_allergen = 0

print(all_cipher_ingredients)
print(safe_cipher)
print(allergens_cipher)

total_safe = 0
for c,p in recipes:
    total_safe += len(c.intersection(safe_cipher))
print(total_safe)
