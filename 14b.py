import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/14.txt', 'r') 
data = [i.strip() for i in file.readlines()]

mask = None
mem = {}

def calc_mask(mask, mem_value_binary):
	output = ""
	# print()
	# print(mem_value_binary)
	# print(mask)
	for i in range(len(mem_value_binary)):
		if mask[i] == "X":
			output = output + "X"
		elif mask[i] == "0":
			output = output + mem_value_binary[i]
		elif mask[i] == "1":
			output = output + "1"

	return output

def generate_all_addresses(address_with_mask):
	out = []
	addresses = [address_with_mask]
	print(addresses)
	while len(addresses) > 0:
		curr_address = addresses.pop()
		offset = curr_address.find('X')
		if offset == -1:
			out.append(curr_address)
		else:
			addr_0 = list(curr_address)
			addr_1 = list(curr_address)
			addr_0[offset] = '0'
			addr_1[offset] = '1'
			addresses.append("".join(addr_0))
			addresses.append("".join(addr_1))
	return out

for line in data:
	mask_re = re.findall("mask = (.*)", line)
	if len(mask_re) > 0:
		mask = mask_re[0]
	else:
		memory_re = re.findall("mem\[(\\d+)\] = (.*)", line)
		mem_address = int(memory_re[0][0])
		mem_address_binary = "{0:b}".format(mem_address).zfill(36)
		mem_int = int(memory_re[0][1])
		mem_value_binary = "{0:b}".format(mem_int).zfill(36)
		address_with_mask = calc_mask(mask, mem_address_binary)
		addresses = generate_all_addresses(address_with_mask)
		addresses_int = list(map(lambda x: int(x, 2), addresses))
		pp.pprint(addresses)
		pp.pprint(addresses_int)
		for a in addresses_int:
			mem[a] = mem_int
		
pp.pprint(mem)

print(sum(mem.values()))