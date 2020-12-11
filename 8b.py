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
	nb_instructions_run = 0
	while 0 <= ip < len(instruction_list) and (nb_instructions_run < len(instruction_list)):
		nb_instructions_run = nb_instructions_run + 1

		(instruction, value) = instruction_list[ip]

		if instruction == "nop":
			ip = ip + 1
		elif instruction == "acc":
			acc = acc + value
			ip = ip + 1
		elif instruction == "jmp":
			ip = ip + value

	return (ip >= len(instruction_list), acc)

instruction_list = parse_program(data)

for (i, v) in enumerate(instruction_list):
	new_instructions = instruction_list.copy()
	if v[0] == "nop":
		new_instructions[i] = ("jmp", instruction_list[i][1])
	elif v[0] == "jmp":
		new_instructions[i] = ("nop", instruction_list[i][1])
	else:
		continue

	result = run_program(new_instructions)
	if result[0]:
		print(result)
