import itertools
import cProfile

# test: 25
# input: 364

lines = open('input.txt', 'r').read().splitlines()
earliest_departure = int(lines[0])
buses = list(map(int, filter(lambda x: x.isnumeric(), lines[1].split(','))))
buses.sort()

earliest = 0, 9999
for b in buses:
    delay = earliest_departure % b
    departure = b - delay
    if (departure < earliest[1]):
        earliest = b, departure

print(earliest)
print("answer: {}".format(earliest[0] * earliest[1]))
