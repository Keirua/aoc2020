from functools import reduce
# input for day 25
card_pk, door_pk = [13135480, 8821721]

# The handshake used by the card and the door involves an operation that transforms a subject number.
# To transform a subject number, start with the value 1.
# Then, a number of times called the loop size, perform the following steps:

#    Set the value to itself multiplied by the subject number.
#    Set the value to the remainder after dividing the value by 20201227.

def update(v, s): return (v * s) % 20201227

def find_secret_loop_size(target, subject_number):
    v = 1
    loop = 0
    while v != target:
        v = update(v, subject_number)
        loop += 1
    return loop

def transform(subject_number, loop_size):
    return reduce(lambda v,_: update(v, subject_number), range(loop_size), 1)
    # equivalent to:
    # v = 1
    # for i in range(loop_size):
    #     v = update(v, subject_number)
    # return v

assert(find_secret_loop_size(5764801, 7) == 8)
assert(find_secret_loop_size(17807724, 7) == 11)
assert(transform(17807724, 8) == transform(5764801, 11))

card_secret_loop_size = find_secret_loop_size(card_pk, 7)
door_secret_loop_size = find_secret_loop_size(door_pk, 7)

encryption_key = transform(door_pk, card_secret_loop_size)
assert(encryption_key == transform(card_pk, door_secret_loop_size))

print(encryption_key)