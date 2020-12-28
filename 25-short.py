from functools import reduce
card_pk, door_pk = [13135480, 8821721]

def update(v, s): return (v * s) % 20201227
def transform(subject_number, loop_size): return reduce(lambda v,_: update(v, subject_number), range(loop_size), 1)

def find_secret_loop_size(target, subject_number):
    v = 1
    loop = 0
    while v != target:
        v = update(v, subject_number)
        loop += 1
    return loop

print(transform(door_pk, find_secret_loop_size(card_pk, 7)))