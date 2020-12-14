import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/14.txt', 'r') 
data = [i.strip() for i in file.readlines()]

mask = None
mem = {}

def calc_mask(mask, mem_value_binary):
	output = ""
	print(mask)
	print(mem_value_binary)
	print()
	for i in range(len(mem_value_binary)):
		if mask[i] == "X":
			output = output + mem_value_binary[i]
		else:
			output = output + mask[i]
	return output

for line in data:
	mask_re = re.findall("mask = (.*)", line)
	if len(mask_re) > 0:
		mask = mask_re[0]
		print(mask)
	else:
		memory_re = re.findall("mem\[(\\d+)\] = (.*)", line)
		mem_address = int(memory_re[0][0])
		mem_int = int(memory_re[0][1])
		mem_value_binary = "{0:b}".format(mem_int).zfill(36)
		print(mem_address, mem_value_binary)
		mem[mem_address] = calc_mask(mask, mem_value_binary)
	
pp.pprint(mem)

non_zeros = list(map(lambda x: int(x, 2), mem.values()))
print(non_zeros)
print(sum(non_zeros))