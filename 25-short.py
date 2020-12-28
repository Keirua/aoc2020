card_pk, door_pk, v, loop_size = 13135480, 8821721, 1, 0
while v != card_pk:
    v, loop_size = (v * 7) % 20201227, loop_size + 1
print(pow(door_pk, loop_size, 20201227))