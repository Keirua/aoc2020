import re
file = open('input/6.txt', 'r') 
data = [i.strip() for i in file.readlines()]


def empty_curr():
	current_answer = {"count": 0}
	for c in "abcdefghijklmnopqrstuvwxyz":
		current_answer[c] = 0
	return current_answer

answers = []
current_answer = empty_curr()
for line in data:
	if line == "":
		answers.append(current_answer)
		current_answer = empty_curr()
	else:
		s = set("".join(line.replace(" ", "")))
		for c in s:
			current_answer[c] += 1
		current_answer["count"] += 1
# special case for the last 
if current_answer != {"count":0}:
	answers.append(current_answer)

print(answers)
p2 = 0
for a in answers:
	for c in a.keys():
		if c != "count" and a[c] == a["count"]:
			p2 += 1
print(p2)

