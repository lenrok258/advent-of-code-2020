import itertools
import copy
from datetime import datetime

# test: 848
# input: 2472

lines = open('input.txt', 'r').read().splitlines()

grid = {}
grid[0] = {}  # w
grid[0][0] = {}  # z
for y, line in enumerate(lines):  # y
    grid[0][0][y] = {}
    for x, c in enumerate(line):  # x
        grid[0][0][y][x] = c


# def print_grid(grid):
#     for z, vz in grid.items():
#         print(f"\nLevel: {z}")

#         for y in range(-3, 6):
#             for x in range(-3, 6):
#                 print(get_value_from_grid(grid, z, y, x), end='')
#             print("")


def get_value_from_grid(grid, w, z, y, x):
    val = grid.get(w, {}).get(z, {}).get(y, {}).get(x, None)
    return val if val else '.'


def set_value_in_grid(grid, w, z, y, x, val):
    if w not in grid:
        grid[w] = {}
    if z not in grid[w]:
        grid[w][z] = {}
    if y not in grid[w][z]:
        grid[w][z][y] = {}
    if x not in grid[w][z][y]:
        grid[w][z][y][x] = val


def get_neighbors(grid, w, z, y, x):
    coordinates = []
    for a in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if a == 0 and i == 0 and j == 0 and k == 0:
                        pass
                    else:
                        value = get_value_from_grid(
                            grid, w + a, z + i, y + j, x + k)
                        coordinates.append((w + a, z + i, y + j, x + k, value))
    return coordinates


def get_all_active(grid):
    active_coordinages = []
    for w, vw in grid.items():
        for z, vz in vw.items():
            for y, yx in vz.items():
                for x, xy in yx.items():
                    if grid[w][z][y][x] == '#':
                        active_coordinages.append((w, z, y, x))
    return active_coordinages


def get_active_count(points_with_values_list):
    return sum([1 if v[4] == '#' else 0 for v in points_with_values_list])


def get_active_count_in_grid():
    count = 0
    for w, vw in grid.items():
        for z, vz in vw.items():
            for y, yx in vz.items():
                for x, xy in yx.items():
                    if grid[w][z][y][x] == '#':
                        count += 1
    return count


def new_state(current_state, active_neighbors_count):
    if current_state == '#':
        if active_neighbors_count in [2, 3]:
            return '#'
        else:
            return '.'
    if current_state == '.':
        if active_neighbors_count == 3:
            return '#'
        else:
            return '.'


def reballance(grid):
    new_grid = {}

    # active cooridinates
    active_ccordinates = get_all_active(grid)
    for ac in active_ccordinates:
        w, z, y, x = ac
        neigbors_zyxwv = get_neighbors(grid, w, z, y, x)
        active_count = get_active_count(neigbors_zyxwv)

        new_st = new_state(get_value_from_grid(grid, w, z, y, x), active_count)
        set_value_in_grid(new_grid, w, z, y, x, new_st)

        # active coordinate neighbors

        for n_wzyxv in neigbors_zyxwv:
            w, z, y, x, v = n_wzyxv
            neigbors_wzyxv_2 = get_neighbors(grid, w, z, y, x)
            active_count_2 = get_active_count(neigbors_wzyxv_2)

            new_st = new_state(get_value_from_grid(
                grid, w, z, y, x), active_count_2)
            set_value_in_grid(new_grid, w, z, y, x, new_st)

    return new_grid


for i in range(6):
    print(datetime.now())
    grid = reballance(grid)

print(get_active_count_in_grid())
