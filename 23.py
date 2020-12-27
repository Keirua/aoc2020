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
        self.mapping = {}
        l = len(data)
        self.mini = None
        self.maxi = None
        for d in data:
            new_node = Node(d)
            self.nodes.append(new_node)
            self.mapping[d] = new_node

            if self.mini is None or d < self.mini:
                self.mini = d
            if self.maxi is None or d > self.maxi:
                self.maxi = d

        for i in range(l):
            self.nodes[i].next = self.nodes[(i+1)%l]
            self.nodes[i].prev = self.nodes[(i- 1+l)%l]

        self.current = self.nodes[0]
    
    def search(self, value):
        """Search for a value, and returns the corresponding node"""
        if value in self.mapping:
            return self.mapping[value]
        return None
        # visited = []
        # curr = self.current
        
        # while curr not in visited:
        #     visited.append(curr)
        #     if curr.value == value:
        #         return curr
        #     curr = curr.next
        # return None

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
        destination = self.search(target_value)
        # print(next3)
        while destination is None or destination in next3:
            target_value -= 1
            if target_value < self.mini:
                target_value = self.maxi
            destination = self.search(target_value)
        
        destination_next = destination.next
        destination.next = next3[0]
        next3[0].prev = destination
        next3[-1].next = destination_next
        destination_next.prev = next3[-1]
        # print(self)
        self.current = self.current.next

    def part1(input, nb_steps):
        data = parse(input)
        nodelist = NodeList(data)
        for i in range(nb_steps):
            nodelist.step()
        return "".join(str(curr.value) for curr in nodelist.all(nodelist.search(1)))[1:]

    def part2(input, nb_steps):
        data = parse(input)
        max_value = max(data)
        new_values = list(range(max_value + 1, 1_000_000 + 1))
        data = data + new_values
        
        nodelist = NodeList(data)
        print("allocated memory")
        for i in range(nb_steps):
            if (i % 100_000) == 0:
                print(100. * float(i) / nb_steps)
            nodelist.step()

        node1 = nodelist.search(1)
        return node1.next.value * node1.next.next.value 

    def __repr__(self):
        return "\n".join(str(curr) for curr in self.all(self.current))

def parse(input):
    data = list(map(int, list(input)))
    return data

assert(NodeList.part1("389125467", 10) == "92658374")
assert(NodeList.part1("389125467", 100) == "67384529")
# assert(NodeList.part2("389125467", 1_000_000) == 149245887792)
print(NodeList.part1(real_input, 100))
print(NodeList.part2(real_input, 10_000_000))