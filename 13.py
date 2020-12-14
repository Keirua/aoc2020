import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = open('input/13.txt', 'r') 
data = [i.strip() for i in file.readlines()]

nearby = int(data[0])
all_shuttles = list(map(int, filter(lambda x: x != "x", data[1].split(','))))

departures = []
for s in all_shuttles:
	closest_departure = (1 + (nearby // s))*(s)
	departures.append(closest_departure)

shortest = min(departures)
min_offset = shortest - nearby
best_shuttle_id = all_shuttles[departures.index(shortest)]

print(min_offset * best_shuttle_id)

