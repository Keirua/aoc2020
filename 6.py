import re
file = open('input/6.txt', 'r') 
data = [i.strip() for i in file.readlines()]


answers = []
current_answer = ""
for line in data:
	if line == "":
		s = set("".join(current_answer.replace(" ", "")))
		answers.append(s)
		current_answer = ""
	else:
		current_answer = current_answer + line
# special case for the last 
if current_answer != "":
	s = set("".join(current_answer.replace(" ", "")))
	answers.append(s)

print(answers)
p1 = 0
for a in answers:
	p1 += len(a)
print(p1)

