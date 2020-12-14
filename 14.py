import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/14ex.txt', 'r') 
data = [i.strip() for i in file.readlines()]

mask = None
mem = [0]*36

for line in data:
	mask_re = re.findall("mask = (.*)", line)
	if len(mask_re) > 0:
		mask = mask_re[0]
		print(mask)
	else:
		memory_re = re.findall("mem\[(\\d+)\] = (.*)", line)
		mem_address = int(memory_re[0][0])
		mem_value_binary = int(memory_re[0][1])
		print(mem_address, mem_value_binary)

	

print(sum(mem))