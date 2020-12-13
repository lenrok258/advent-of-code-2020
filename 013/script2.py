import itertools
import cProfile

# test: 25
# input: 364

lines = open('input_test1.txt', 'r').read().splitlines()
earliest_departure = int(lines[0])
buses = list(map(int, map(lambda x: 0 if x == 'x' else x, lines[1].split(',') )))
buses.sort()

print(buses)
