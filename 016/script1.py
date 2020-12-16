import re

# test: 71
# input: 26869

validations = {}
my_ticket = []
tickets = []
invalid_sum = 0

input_blocks = open('input.txt', 'r').read().split("\n\n")
for line in input_blocks[0].splitlines():
    tiles = re.split(": | or ", line)
    validations[tiles[0]] = (tiles[1], tiles[2])
for line in input_blocks[1].splitlines()[1:]:
    my_ticket = line.split(',')
for line in input_blocks[2].splitlines()[1:]:
    tickets.append(line.split(','))


print(validations)
print(my_ticket)
print(tickets)
print("------")


def is_valid(val):
    for valid_key, valid_values in validations.items():
        for vv in valid_values:
            v_min, v_max = map(int, vv.split("-"))
            if (v_min <= int(val) <= v_max):
                return True
    return False


def is_all_valid(tic):
    for v in tic:
        if not is_valid(v):
            global invalid_sum
            invalid_sum = invalid_sum + int(v)


for tic in tickets:
    is_all_valid(tic)


print(invalid_sum)
