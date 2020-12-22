import re
file = open('input/22.txt', 'r') 
import pprint
pp = pprint.PrettyPrinter(indent=4)
from collections import defaultdict, deque

data = [i.strip() for i in file.readlines()]

players = [
	deque(),
	deque()
]
player_id = 0
for line in data:
	if str(line).find("Player") > -1:
		continue
	if line == "":
		player_id += 1
	else:
		players[player_id].appendleft(int(line))

pp.pprint(players)

def compute_score(player):
	total = 0
	for i,v in enumerate(player):
		total += (i+1) * v
	return total

def run_game(players):
	while True:
		top0 = players[0].pop()
		top1 = players[1].pop()
		cards = [max(top0, top1), min(top0, top1)]
		assert(top0 != top1)
		if top0 > top1:
			players[0].appendleft(cards[0])
			players[0].appendleft(cards[1])
		elif top1 > top0:
			players[1].appendleft(cards[0])
			players[1].appendleft(cards[1])
		if len(players[0]) == 0:
			return compute_score(players[1])
		if len(players[1]) == 0:
			return compute_score(players[0])

score = run_game(players)
print(score)
pp.pprint(players)