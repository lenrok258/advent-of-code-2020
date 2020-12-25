
# test: 14897079
# input: 9855013 (too high)

lines = open('input.txt', 'r').read().splitlines()

pub_card, pub_door = map(int, lines)

def find_loop_size(pub_key):
    curr = 1
    for i in range(1, 100000001): 
        curr = (curr * 7) % 20201227
        # print(f"{i}: {curr}")
        if curr == pub_key:
            # print("got it!")
            return i


def produce_enc_key(pub_key, loop_size):
    curr = 1
    for i in range(1, loop_size + 1):
        # print(f"{i}: {curr}")
        curr = (curr * pub_key) % 20201227
    return curr


loop_size_card = find_loop_size(pub_card)
loop_size_door = find_loop_size(pub_door)

# print(loop_size_card, loop_size_door)

enc_key_card = produce_enc_key(pub_door, loop_size_card)
enc_key_door = produce_enc_key(pub_card, loop_size_door)

print(enc_key_card)
print(enc_key_door)

