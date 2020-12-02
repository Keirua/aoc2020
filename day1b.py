file = open('input/1.txt', 'r') 
data = [int(i.strip()) for i in file.readlines()]

def pair_that_sum_to(v):
	for d in data:
		other = v - d
		if other in data:
			return [d, other]
	return []

for d in data:
	sum2 = 2020 - d
	partial_sum = pair_that_sum_to(sum2)
	if len(partial_sum) > 0:
		print(d, partial_sum)
		print(d * partial_sum[0] * partial_sum[1])
		break
