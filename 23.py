import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

sample_input = "389125467"
real_input = "853192647"


class Node:
	def __init__(self, v = None):
		self.value = v
		self.prev = None
		self.next = None

	def __repr__(self):
		return "{} = {} - prev = {}, next = {}".format(id(self), self.value, id(self.prev), id(self.next))

class NodeList:
	def __init__(self, data):
		self.data = data
		self.nodes = []
		l = len(data)
		for d in data:
			self.nodes.append(Node(d))
		for i in range(l):
			self.nodes[i].next = self.nodes[(i+1)%l]
			self.nodes[i].prev = self.nodes[(i-1+l)%l]
	
	def __repr__(self):
		return "\n".join(str(s) for s in self.nodes)

def parse(input):
	data = list(map(int, list(input)))
	return data, NodeList(data)


def run_game(cups, nb_turns):
	cups,nodelist = parse(cups)
	for curr_turn in range(nb_turns):
		next3 = [cups[(curr_turn+ 1+i) % len(cups)] for i in range(3)]
		print("-- move {}--".format(curr_turn+1))
		print("{}".format(", ".join(map(str, cups))))
		print("{}".format("{}^".format(" "*3*(curr_turn%len(cups)))))
		print("{}".format(next3))

		destination = cups[curr_turn%len(cups)]-1
		print("curr_turn = {}".format(curr_turn))
		print("destination = {}".format(destination))
		for n in next3:
			cups.remove(n)

		while destination in next3:
			destination -= 1
			if destination <= min(cups):
				destination = max(cups)
			print("destination = {}".format(destination))
		if destination < min(cups):
			destination = max(cups)
		print("destination: {}".format(destination))
		# first_cups = cups[:curr_turn+1]
		# last_cups = cups[curr_turn+1+3:]
		# new_cups = first_cups + last_cups

		offset = cups.index(destination)
		print(offset)
		for i in range(3):
			cups.insert((offset+i+1), next3[i])
		# print(new_cups)
		# print()
		# cups = new_cups
		print("after")
		print(", ".join(map(str, cups)))
		print()
		print()
	return "".join(map(str, cups))

# deck = parse(sample_input)
# deck = parse(real_input)

cups,nodelist = parse(sample_input)
pp.pprint(nodelist)

# assert(run_game("389125467", 10) == "92658374")
# assert(run_game("389125467", 100) == "67384529")
# print(run_game(sample_input, 10))