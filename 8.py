import re
file = open('input/8.txt', 'r') 
data = [i.strip() for i in file.readlines()]

NOP = 0
ACC = 1
JMP = 2



def parse_program(data):
	instruction_list = []
	for line in data:
		parsed = line.split(" ")
		instruction = parsed[0]
		amount = int(parsed[1])
		instruction_list.append((instruction, amount))

	return instruction_list

def run_program(instruction_list):
	acc = 0
	ip = 0
	visited = [False] * len(instruction_list)

	while visited[ip] == False:
		visited[ip] = True
		(instruction, value) = instruction_list[ip]

		if instruction == "nop":
			ip = ip + 1
		elif instruction == "acc":
			acc = acc + value
			ip = ip + 1
		elif instruction == "jmp":
			ip = ip + value

	return acc


instruction_list = parse_program(data)
print(instruction_list)
print(run_program(instruction_list))