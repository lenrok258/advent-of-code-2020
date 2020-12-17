import itertools
import copy
from datetime import datetime

# test: 112
# input: 353

lines = open('input.txt', 'r').read().splitlines()

grid = {}
grid[0] = {}
for x, line in enumerate(lines):
    grid[0][x] = {}
    for y, c in enumerate(line):
        grid[0][x][y] = c


def print_grid(grid):
    for z, vz in grid.items():
        print(f"\nLevel: {z}")

        for y in range(-3, 6):
            for x in range(-3, 6):
                print(get_value_from_grid(grid, z, y, x), end='')
            print("")


def get_value_from_grid(grid, z, y, x):
    val = grid.get(z, {}).get(y, {}).get(x, None)
    return val if val else '.'


def set_value_in_grid(grid, z, y, x, val):
    if z not in grid:
        grid[z] = {}
    if y not in grid[z]:
        grid[z][y] = {}
    if x not in grid[z][y]:
        grid[z][y][x] = val


def get_neighbors(grid, z, y, x):
    coordinates = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if i == 0 and j == 0 and k == 0:
                    pass
                else:
                    value = get_value_from_grid(grid, z + i, y + j, x + k)
                    coordinates.append((z + i, y + j, x + k, value))
    return coordinates


def initialize_empty_if_not_present(z, y, x):
    set_value_in_grid(grid, z, y, x, '.')


def get_all_active(grid):
    active_coordinages = []
    for z, vz in grid.items():
        for y, yx in vz.items():
            for x, xy in yx.items():
                if grid[z][y][x] == '#':
                    active_coordinages.append((z, y, x))
    return active_coordinages


def get_active_count(points_with_values_list):
    return sum([1 if v[3] == '#' else 0 for v in points_with_values_list])


def get_active_count_in_grid():
    count = 0
    for z, vz in grid.items():
        for y, yx in vz.items():
            for x, xy in yx.items():
                if grid[z][y][x] == '#':
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
        z, y, x = ac
        neigbors_zyxv = get_neighbors(grid, z, y, x)
        active_count = get_active_count(neigbors_zyxv)

        new_st = new_state(get_value_from_grid(grid, z, y, x), active_count)
        set_value_in_grid(new_grid, z, y, x, new_st)

        # active coordinate neighbors

        for n_zyxv in neigbors_zyxv:
            z, y, x, v = n_zyxv
            neigbors_zyxv_2 = get_neighbors(grid, z, y, x)
            active_count_2 = get_active_count(neigbors_zyxv_2)

            new_st = new_state(get_value_from_grid(
                grid, z, y, x), active_count_2)
            set_value_in_grid(new_grid, z, y, x, new_st)

    return new_grid


print_grid(grid)
for i in range(6):
    print(datetime.now())
    grid = reballance(grid)

print(get_active_count_in_grid())