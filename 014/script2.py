import itertools
import cProfile
import functools
import math

# test: 208
# input: 3260587250457


def parse_input_line(line):
    tiles = line.split(' = ')
    if tiles[0] == 'mask':
        return tiles
    else:
        mem_addr = tiles[0].split("[")[1].split("]")[0]
        return (int(mem_addr), int(tiles[1]))


def compute_adresses(mask, address):
    mask_or = int(mask.replace('X', '0'), 2)
    address |= mask_or

    x_bits = itertools.product(['0', '1'], repeat=mask.count('X'))
    address_str = bin(address).replace('0b', '').rjust(36, '0')
    addresses = list()
    for xb in x_bits:
        single_res = ""
        for im, cm in enumerate(mask):
            if cm == 'X':
                single_res += xb[0]
                xb = xb[1:]
            else:
                single_res += address_str[im]
        addresses.append(single_res)
    return map(lambda a: int(a, 2), addresses)


def initialize_program(commands):
    memory = dict()
    curr_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    for c in commands:
        instr, value = c
        if instr == 'mask':
            curr_mask = value
        else:
            for addr in compute_adresses(curr_mask, instr):
                memory[addr] = value
    return memory


commands = map(parse_input_line, open('input.txt', 'r').read().splitlines())

memory = initialize_program(commands)

print(sum(memory.values()))
