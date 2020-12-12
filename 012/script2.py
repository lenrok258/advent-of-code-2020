import itertools
import cProfile
import math

# test: 286
# input: 39518


def rotate_point(point, angle):
    angle = math.radians(angle) * -1
    return (round(point[0]*math.cos(angle)-point[1]*math.sin(angle)),
            round(point[0]*math.sin(angle)+point[1]*math.cos(angle)))


def parse_command(input):
    return (input[:1], int(input[1:]))


def navigate(commands):

    waypoint = {'EW': 10, 'NS': 1}
    moves_counter = {'EW': 0, 'NS': 0}

    for c in commands:
        code, value = c

        if code == 'F':
            moves_counter['EW'] += value * waypoint['EW']
            moves_counter['NS'] += value * waypoint['NS']

        elif code in ['E', 'W', 'N', 'S']:
            if code == 'E':
                waypoint['EW'] += value
            if code == 'W':
                waypoint['EW'] -= value
            if code == 'N':
                waypoint['NS'] += value
            if code == 'S':
                waypoint['NS'] -= value

        elif code in ['R', 'L']:
            if code == 'L':
                value = 360 - value

            waypoint['EW'], waypoint['NS'] = rotate_point(
                (waypoint['EW'], waypoint['NS']), value)

    return moves_counter


commands = map(parse_command, open('input.txt', 'r').read().splitlines())

result = navigate(commands)

print(abs(result['EW']) + abs(result['NS']))
