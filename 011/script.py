import itertools
import cProfile
import copy

# test: 37

def count_occupied(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                count += 1
    return count

def is_seat_taken(seats, y, x):
    if y < 0 or x < 0 or y >= len(seats) or x >= len(seats[y]):
        return 0
    if seats[y][x] == '#':
        # print("return {},{}={}".format(y,x,1))
        return 1
    # print("return {},{}={}".format(y,x,0))
    return 0


def number_of_adjacent(seats, y, x):
    return is_seat_taken(seats, y-1, x-1) + \
        is_seat_taken(seats, y-1, x) + \
        is_seat_taken(seats, y-1, x+1) + \
        is_seat_taken(seats, y, x+1) + \
        is_seat_taken(seats, y+1, x+1) + \
        is_seat_taken(seats, y+1, x) + \
        is_seat_taken(seats, y+1, x-1) + \
        is_seat_taken(seats, y, x-1)


def is_seat_ok(seats, y, x):
    seat = seats[y][x]
    adjacent_count = number_of_adjacent(seats, y, x)
    # print(f"seat={seat}, adjc={adjacent_count}")
    if seat == 'L' and adjacent_count == 0:
        return True
    if seat == '#' and adjacent_count < 4:
        return True
    return False

def reballance(seats):
    new_seats = copy.deepcopy(seats)
    for y, row in enumerate(seats):
        for x, column in enumerate(row):
            if seats[y][x] == '.':
                pass
            elif is_seat_ok(seats, y, x):
                new_seats[y][x] = '#'
            else:
                new_seats[y][x] = 'L'
    return new_seats

def print_ferry(seats):
    print("")
    for s in seats:
        print(s)
    print("")


lines = open('input.txt', 'r').read().splitlines()
seats = list()
for l in lines:
    row = list(l)
    seats.append(row)

prv_ferry = None
ferry = seats
while ferry != prv_ferry:
    prv_ferry = ferry
    ferry = reballance(ferry)
    # print_ferry(ferry)

print_ferry(ferry)
print(count_occupied(ferry))