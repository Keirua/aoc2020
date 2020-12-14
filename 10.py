import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/10ex.txt', 'r') 
data = [int(i.strip()) for i in file.readlines()]

pp.pprint(data)



