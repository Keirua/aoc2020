import re
file = open('input/24ex.txt', 'r') 
import pprint
pp = pprint.PrettyPrinter(indent=4)
from collections import defaultdict, deque

data = [i.strip() for i in file.readlines()]

for line in data:
	directions = re.findall("e|w|ne|nw|se|sw", line)
	print(line, directions)
