import itertools
import cProfile
import functools

# test: 165
# input: 15403588588538


def to_binary_string(intput_int):
    return format(intput_int, '#036b')


def parse_input_line(line):
    tiles = line.split(' = ')
    if tiles[0] == 'mask':
        return tiles
    else:
        mem_addr = tiles[0].split("[")[1].split("]")[0]
        return (int(mem_addr), int(tiles[1]))


def apply_mask(mask, value):
    and_mask = mask.replace('X', '1')
    or_mask = mask.replace('X', '0')
    return value & int(and_mask, 2) | int(or_mask, 2)


def initialize_program(commands):

    memory = dict()
    curr_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    for c in commands:
        instr, value = c
        if instr == 'mask':
            curr_mask = value
        else:
            memory[instr] = apply_mask(curr_mask, value)

    return memory


commands = map(parse_input_line, open('input.txt', 'r').read().splitlines())

memory = initialize_program(commands)

print(sum(memory.values()))
