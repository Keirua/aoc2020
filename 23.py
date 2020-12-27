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
		"""Initializes the node from a list of data"""
		self.data = data
		self.nodes = []

		l = len(data)
		for d in data:
			self.nodes.append(Node(d))
		for i in range(l):
			self.nodes[i].next = self.nodes[(i+1)%l]
			self.nodes[i].prev = self.nodes[(i-	1+l)%l]
		self.current = self.nodes[0]
	
	def search(self, value):
		"""Search for a value, and returns the corresponding node"""
		visited = []
		curr = self.current
		
		while curr not in visited:
			visited.append(curr)
			if curr.value == value:
				return curr
			curr = curr.next
		return None

	def mini_maxi(self):
		mini, maxi = None, None
		for n in self.all(self.current):
			if mini is None or n.value < mini:
				mini = n.value
			if maxi is None or n.value > maxi:
				maxi = n.value

		return mini, maxi

	def all(self, start):
		visited = []
		curr = start
		
		while curr not in visited:
			visited.append(curr)
			curr = curr.next
		return visited

	def remove_next_3(self):
		next3 = [self.current.next, self.current.next.next, self.current.next.next.next]
		
		new_next = next3[-1].next
		self.current.next = new_next
		new_next.prev = self.current

		return next3

	def step(self):
		next3 = self.remove_next_3()
		target_value = self.current.value - 1
		destination = None
		mini, maxi = self.mini_maxi()
		while destination is None:
			destination = self.search(target_value)
			target_value -= 1
			if target_value < mini:
				target_value = maxi
		
		destination_next = destination.next
		destination.next = next3[0]
		next3[0].prev = destination
		next3[-1].next = destination_next
		destination_next.prev = next3[-1]
		# print(self)
		self.current = self.current.next

	def part1(input, nb_steps):
		cups,nodelist = parse(input)
		for i in range(nb_steps):
			nodelist.step()
		return "".join(str(curr.value) for curr in nodelist.all(nodelist.search(1)))[1:]

	def __repr__(self):
		return "\n".join(str(curr) for curr in self.all(self.current))

def parse(input):
	data = list(map(int, list(input)))
	return data, NodeList(data)

assert(NodeList.part1("389125467", 10) == "92658374")
assert(NodeList.part1("389125467", 100) == "67384529")
print(NodeList.part1(real_input, 100))