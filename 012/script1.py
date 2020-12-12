import itertools
import cProfile

# test: 25
# input: 364

compass = ['E', 'S', 'W', 'N']


def rotation(c):
    move_code, move_value = c

    ret = move_value / 90
    if move_code == 'L':
        ret *= -1

    return int(ret)


def parse_command(input):
    return (input[:1], int(input[1:]))


def navigate(commands):
    moves_counter = {
        'E': 0,
        'W': 0,
        'N': 0,
        'S': 0
    }

    facing = 'E'

    for c in commands:
        move_code, move_value = c

        if move_code == 'F':
            moves_counter[facing] += move_value
        elif move_code in ['E', 'W', 'N', 'S']:
            moves_counter[move_code] += move_value
        elif move_code in ['R', 'L']:
            rottor = rotation(c)
            compass_idx = compass.index(facing)
            new_compass_idx = (compass_idx + rottor) % 4
            facing = compass[new_compass_idx]

    return moves_counter


commands = map(parse_command, open('input.txt', 'r').read().splitlines())

result = navigate(commands)

deltaEW = abs(result['E'] - result['W'])
deltaNS = abs(result['N'] - result['S'])

print(deltaEW + deltaNS)
