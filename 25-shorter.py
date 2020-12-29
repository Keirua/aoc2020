card_pk, door_pk = 13135480,8821721
v = 1
encoding = 1
while v != card_pk:
	v, encoding = v*7%20201227, encoding*door_pk % 20201227
print(encoding)