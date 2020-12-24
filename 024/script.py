import re
import copy

# test - star 1: 10 
# test - star 2: 2208
# input - star 1: 436
# input - star 2: 

lines = open('input.txt', 'r').read().splitlines()
directions = [re.findall("(sw|se|nw|ne|w|e)", l) for l in lines]

floor = {}

for d in directions:
    tile_coordin = [0, 0]
    for c in d:
        if c == 'w':
            tile_coordin[0] -= 2
        if c == 'nw':
            tile_coordin[0] -= 1
            tile_coordin[1] += 1
        if c == 'ne':
            tile_coordin[0] += 1
            tile_coordin[1] += 1
        if c == 'e':
            tile_coordin[0] += 2
        if c == 'se':
            tile_coordin[0] += 1
            tile_coordin[1] -= 1
        if c == 'sw':
            tile_coordin[0] -= 1
            tile_coordin[1] -= 1
        
    tile_key = str(tile_coordin[0]) + "_" + str(tile_coordin[1])

    if tile_key not in floor:
        floor[tile_key] = 'B'
    else:
        color = floor[tile_key]
        floor[tile_key] = 'W' if color == 'B' else 'W'

def count_blacks(floor):
    return sum(map(lambda v: 1 if v == 'B' else 0, floor.values()))

print(f"Star 1: {count_blacks(floor)}")

# Star 2

adj_moves = [(2,0), (1,1), (-1,1), (-2,0), (-1,-1), (1,-1)]


def get_adjacents(floor, tile_coordin):
    adjs = []
    coor_tuple = tile_coordin.split('_')
    for move in adj_moves:
        n_x = int(coor_tuple[0]) + move[0]
        n_y = int(coor_tuple[1]) + move[1]
        n_coor = str(n_x) + "_" + str(n_y)
        adjs.append(n_coor)
    return adjs

def get_number_of_black_adjacents(floor, tile_coordin):
    count = 0
    coor_tuple = tile_coordin.split('_')
    for move in adj_moves:
        n_x = int(coor_tuple[0]) + move[0]
        n_y = int(coor_tuple[1]) + move[1]
        n_coor = str(n_x) + "_" + str(n_y)
        color = floor.get(n_coor, 'W')
        if color == 'B':
            count += 1
    return count


def flip_floor(floor):
    new_floor = copy.deepcopy(floor)

    for k, v in floor.items():
        blacks = get_number_of_black_adjacents(floor, k)
        if v == 'W' and blacks == 2:
            new_floor[k] = 'B'
        if v == 'B' and (blacks == 0 or blacks > 2):
            new_floor[k] = 'W'

        for nk in get_adjacents(floor, k):
            nblacks = get_number_of_black_adjacents(floor, nk)
            nv = floor.get(nk, 'W')
            if nv == 'W' and nblacks == 2:
                new_floor[nk] = 'B'
            if nv == 'B' and (nblacks == 0 or nblacks > 2):
                new_floor[nk] = 'W'

    return new_floor


# print(f"Day 0: {count_blacks(floor)}")
for i in range(1,101):
    floor = flip_floor(floor) 
    print(f"Day {i}: {count_blacks(floor)}")