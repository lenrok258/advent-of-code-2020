import re

# test: 71
# input: 26869

validations, my_ticket, tickets = {}, [], []

input_blocks = open('input.txt', 'r').read().split("\n\n")
for line in input_blocks[0].splitlines():
    tiles = re.split(": | or ", line)
    validations[tiles[0]] = (tiles[1], tiles[2])
for line in input_blocks[1].splitlines()[1:]:
    my_ticket = line.split(',')
for line in input_blocks[2].splitlines()[1:]:
    tickets.append(line.split(','))


def is_valid(val):
    for valid_key, valid_values in validations.items():
        for vv in valid_values:
            v_min, v_max = map(int, vv.split("-"))
            if (v_min <= int(val) <= v_max):
                return True
    return False


def sum_invalid_fields_in_ticket(ticket):
    return sum([int(v) if not is_valid(v) else 0 for v in ticket])


answer = sum(map(sum_invalid_fields_in_ticket, tickets))
print(answer)
