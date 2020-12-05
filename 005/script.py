import re

input_file = open('input.txt', 'r')
lines = input_file.readlines()


def decode(encoded_input, floor, celing):
    # print("{} {} {}".format(encoded_input, floor, celing))

    if floor == celing:
        return floor

    cutting_point = floor + int((celing - floor + 1) / 2)
    encoded_letter = encoded_input[0]
    if encoded_letter == 'F' or encoded_letter == 'L':
        return decode(encoded_input[1:], floor, cutting_point - 1)
    else:
        return decode(encoded_input[1:], cutting_point, celing)


def decode_seat_coordinates(line):
    row = decode(line[:7], 0, 127)
    column = decode(line[7:], 0, 7)
    return (row, column)


def create_2d_array():
    result = list()
    for i in range(0, 127):
        result.append([0, 0, 0, 0, 0, 0, 0, 0])
    return result


seat_id_max = 0
seats_array_2d = create_2d_array()
for line in lines:
    line = line.replace('\n', '')

    seat_touple = decode_seat_coordinates(line)
    seat_id = seat_touple[0] * 8 + seat_touple[1]

    seats_array_2d[seat_touple[0]][seat_touple[1]] = 1

    if seat_id > seat_id_max:
        seat_id_max = seat_id

    print("Touple: {}, seat id:{}\n".format(seat_touple, seat_id))

print("Answer star 1: {}".format(seat_id_max))


# Start 2 bellow

for col in seats_array_2d:
    print(col)


# row: 69, 5