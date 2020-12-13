import itertools
import cProfile
import math

# test 1: 1068781
# input: 213890632230818

lines = open('input.txt', 'r').read().splitlines()
buses = list(map(int, map(lambda x: 0 if x == 'x' else x, lines[1].split(',') )))

print(buses)

def check_number(number, bus, bus_idx):
    return (number + bus_idx) % bus == 0
    

def win_a_grand_price():

    step = buses[0]
    idx = 0
    for i, bus in enumerate(buses, start=1):
        
        if i == len(buses):
            break

        buses_to_solve = buses[:i+1]
        print(f"Computing for: {buses_to_solve}")

        if buses_to_solve[-1] == 0:
            continue

        while True:
            idx += step 
            if check_number(idx, buses_to_solve[-1], i):
                print(f"solution={idx}")
                step = math.lcm(*map(lambda b: b if b>0 else 1, buses_to_solve))
                print(f"step: {step}\n")
                break


win_a_grand_price()
