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

def hash_hand(hand):
	return ",".join(map(str, hand))

def hash_hands(players):
	return "{}-{}".format(hash_hand(players[0]), hash_hand(players[1]))

def display_state(players, depth, nb_rounds):
	tabs = "\t" * (depth-1)
	print("{}-- Round {} (Game {}) --".format(tabs, nb_rounds, depth))
	print("{}Player’s 1 deck: {}".format(tabs, hash_hand(players[0])))
	print("{}Player’s 2 deck: {}".format(tabs, hash_hand(players[1])))

	print("{}Player’s 1 plays: {}".format(tabs, players[0][-1]))
	print("{}Player’s 2 plays: {}".format(tabs, players[1][-1]))

	print()

def run_game_recursive(players, hashes=[], depth=0):
	nb_rounds = 0
	while True:
		nb_rounds = nb_rounds +1
		# Before either player deals a card, if there was a previous round
		# in this game that had exactly the same cards in the same order
		# in the same players' decks, the game instantly ends
		# in a win for player 1.
		hashed_hand = hash_hands(players)
		if hashed_hand in hashes:
			return compute_score(players[0]), 0
		hashes.append(hashed_hand)
		# display_state(players, depth, nb_rounds)

		top0 = players[0].pop()
		top1 = players[1].pop()
		cards = [max(top0, top1), min(top0, top1)]
		if len(players[0]) < top0 or len(players[1]) < top1:
			# at least one player must not have enough cards left in their deck
			# to recurse; the winner of the round is the player with the higher-value card.
			winner = 0
			if top1 > top0:
				winner = 1
			players[winner].appendleft(cards[0])
			players[winner].appendleft(cards[1])
			if len(players[0]) == 0:
				return compute_score(players[1]), 1
			if len(players[1]) == 0:
				return compute_score(players[0]), 0
			continue
		# If both players have at least as many cards remaining in their deck
		# as the value of the card they just drew, the winner of the round is determined
		# by playing a new game of Recursive Combat.
		sub_cards0 = deque([players[0][-(i+1)] for i in range(top0)][::-1])
		sub_cards1 = deque([players[1][-(i+1)] for i in range(top1)][::-1])
		score, winner = run_game_recursive([sub_cards0, sub_cards1], [], depth+1)
		
		if winner == 0:
			players[0].appendleft(top0)
			players[0].appendleft(top1)
		elif winner == 1:
			players[1].appendleft(top1)
			players[1].appendleft(top0)

		if len(players[0]) == 0:
			return compute_score(players[1]), 1
		if len(players[1]) == 0:
			return compute_score(players[0]), 0

# score = run_game(players)
# print(score)

score2, winner = run_game_recursive(players, [], 1)
# 34931 is too low
print(score2, winner)