import re
file = open('input/22.txt', 'r') 
import pprint
pp = pprint.PrettyPrinter(indent=4)
from collections import defaultdict

data = [i.strip() for i in file.readlines()]

players = [
	[],
	[]
]
player_id = 0
for line in data:
	if str(line).find("Player") > -1:
		continue
	if line == "":
		player_id += 1
	else:
		players[player_id].append(int(line))

pp.pprint(players)
