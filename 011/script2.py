import itertools
import cProfile

# test: 26

# R RD D DL L LU U UR

moves = {
    'R': [0, 1],
    'DR': [1, 1],
    'D': [1, 0],
    'DL': [1, -1],
    'L': [0, -1],
    'UL': [-1, -1],
    'U': [-1, 0],
    'UR': [-1, 1]
}


def cache_key(direction, y, x):
    return direction + "|" + str(y) + "|" + str(x)


def anyone_in_direction(seats, direction, y, x):
    move = moves[direction]
    y_moved = y+move[0]
    x_moved = x+move[1]

    if y_moved < 0 or (y_moved == len(seats)) or x_moved < 0 or x_moved == len(seats[y]):
        return True
    elif seats[y_moved][x_moved] == '#':
        return False
    elif seats[y_moved][x_moved] == 'L':
        return True
    else:
        answer = anyone_in_direction(seats, direction, y_moved, x_moved)
        return answer


def count_people(seats, y, x):
    people_count = 0
    for direction in moves.keys():
        is_ok = anyone_in_direction(seats, direction, y, x)
        if not is_ok:
            people_count += 1
    return people_count


def is_seat_ok(seats, y, x):
    people_count = count_people(seats, y, x)
    if seats[y][x] == 'L' and people_count == 0:
        return True
    if seats[y][x] == '#' and people_count < 5:
        return True
    return False


def reballance(seats):
    new_ferry = list()
    for y, row in enumerate(seats):

        new_row = list()
        for x, seat in enumerate(row):

            if seat == '.':
                new_row.append('.')
            else:
                ok = is_seat_ok(seats, y, x)
                if ok:
                    new_row.append('#')
                else:
                    new_row.append('L')
        new_ferry.append(new_row)
    return new_ferry


def print_ferry(seats):
    print("")
    for s in seats:
        print(s)
    print("")


def count_occupied(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                count += 1
    return count


lines = open('input.txt', 'r').read().splitlines()
seats = list()
for l in lines:
    row = list(l)
    seats.append(row)

prv = seats
curr = seats
while True:
    curr = reballance(curr)

    if curr == prv:
        break

    prv = curr

print_ferry(curr)
print(count_occupied(curr))
