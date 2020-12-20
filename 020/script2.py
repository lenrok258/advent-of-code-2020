

# test: 273
# input: 1836

# BLOCK_WIDTH = 10

blocks = open('input.txt', 'r').read().split("\n\n")

imgs_ids, imgs_data = [], []

for b in blocks:
    b = b.splitlines()
    title = b[0].replace("Tile ", "").replace(":", "")
    imgs_ids.append(title)

    img_data = [] 
    for line in b[1:]:
        img_data.append(line.replace("\n", ""))
    imgs_data.append(img_data)

# -------------------------------------------

for i, data in enumerate(imgs_data):
    print(f"{i} {imgs_ids[i]}: {data}")
print("")

# -------------------------------------------

def print_img(idx):
    data = imgs_data[idx]
    for d in data:
        print(d)

def print_img_data(data):
    for d in data:
        print(d)

# 0: top, 1: right, 2: bottom, 3: left
def extract_edges(img_idx):
    # print(img_idx)
    edges = []
    data = imgs_data[img_idx]
    edges.append(data[0]) # top
    left, right = "", ""
    for line in data:
        right += line[-1] 
        left += line[0] 
    edges.append(right) # right
    edges.append(data[-1]) # bottom
    edges.append(left) # left
    return edges

def extract_edges_data(data):
    edges = []
    edges.append(data[0]) # top
    left, right = "", ""
    for line in data:
        right += line[-1] 
        left += line[0] 
    edges.append(right) # right
    edges.append(data[-1]) # bottom
    edges.append(left) # left
    return edges

def flip_edge(edge):
    return edge[::-1]


def are_compatibile(m_edge, s_edge):
    if m_edge == s_edge:
        return True
    if m_edge == flip_edge(s_edge):
        return True
    return False


def is_corner(img_idx):
    m_data = imgs_data[img_idx]
    m_edges = extract_edges(img_idx)

    compatibile_count = 0
    for i, img_id in enumerate(imgs_ids):
        if i == img_idx:
            continue
         
        s_edges = extract_edges(i)
        for m_e in m_edges:
            for s_e in s_edges:
                # print(m_e, s_e, are_compatibile(m_e, s_e))
                if are_compatibile(m_e, s_e):
                    compatibile_count += 1

    if compatibile_count == 2:
        return True

    # print("==========")
    
    return False


def get_corners():
    corners_idxs = []
    for i, img_idx in enumerate(imgs_ids):
        if is_corner(i):
            corners_idxs.append(i)
    return corners_idxs



def get_matching_puzzle(puzzle_idx, direction):
    m_edge = extract_edges(puzzle_idx)[direction]
    for i, img_id in enumerate(imgs_ids):
        if i == puzzle_idx:
            continue

        s_edges = extract_edges(i)
        for s_e in s_edges:
            if are_compatibile(m_edge, s_e):
                return i


# upside down
def flip_hor(data):
    return data[::-1]


# clockwise, 90deg
def rotate(data):
    new_data = [""] * len(data)
    for i, line in enumerate(reversed(data)):
        for j, c in enumerate(line): 
            new_data[j] += c
    return new_data


def rotate_corner_to_make_it_left_up(idx):
    data = imgs_data[idx]
    new_data = data

    new_data = flip_hor(new_data)
    imgs_data[idx] = new_data

    for i in range(4):
        if get_matching_puzzle(idx, 1) != None and get_matching_puzzle(idx, 2) != None:
            return 
        new_data = rotate(new_data)
        imgs_data[idx] = new_data
    
    new_data = flip_hor(new_data)
    imgs_data[idx] = new_data

    for i in range(4):
        if get_matching_puzzle(idx, 1) != None and get_matching_puzzle(idx, 2) != None:
            return
        new_data = rotate(new_data)
        imgs_data[idx] = new_data


def rotate_matching(idx_from, direction, idx_to):
    m_edge = extract_edges(idx_from)[direction]
    complementary_direction = (direction + 2) % 4
    
    for i in range(4):
        s_edge = extract_edges(idx_to)[complementary_direction]
        if m_edge == s_edge:
            return
        imgs_data[idx_to] = rotate(imgs_data[idx_to])
    
    imgs_data[idx_to] = flip_hor(imgs_data[idx_to])

    for i in range(4):
        s_edge = extract_edges(idx_to)[complementary_direction]
        if m_edge == s_edge:
            return
        imgs_data[idx_to] = rotate(imgs_data[idx_to]) 
            

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

def solve_puzzle():

    solution = []

    random_corner = get_corners()[0]
    rotate_corner_to_make_it_left_up(random_corner)

    solution_line = []
    solution_line.append(random_corner)
    solution.append(solution_line)

    while True:
        while True:
            last_line = solution[-1]
            current_idx = last_line[-1]
            matching = get_matching_puzzle(current_idx, 1)

            if matching == None: # no more puzzles going left
                break

            rotate_matching(current_idx, 1, matching)
            last_line.append(matching)
        
        last_line = solution[-1]
        first_left = last_line[0]

        # find puzzle going down
        matching = get_matching_puzzle(first_left, 2)

        if matching == None: # no more puzzles going down
            break

        rotate_matching(first_left, 2, matching)

        new_line = []
        new_line.append(matching)
        solution.append(new_line)



    return solution


def drop_edges(data):
    new_data = []
    for line in data[1:-1]:
        new_data.append(line[1:-1])
    return new_data


def print_raster(raster):
    for line in raster:
        print("".join(line))

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

puzzles_order = solve_puzzle()

for i in puzzles_order:
    for j in i:
        print(f"{imgs_ids[j]} " , end='')
    print()
print()


raster = []
for i in range((len(imgs_data[0]) - 2) * len(puzzles_order)):
    raster.append([])

for j, line in enumerate(puzzles_order):
    raster_shift = 0 + j*(len(imgs_data[0]) - 2)
    for puzzle_idx in line:
        raw_data = drop_edges(imgs_data[puzzle_idx])
        for i, raw_line in enumerate(raw_data):
            raster[i + raster_shift].extend(raw_line)

print_raster(raster)

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# (down, right)
monster_path = [(1, 1), (0, 3), (-1, 1), (0, 1), (1, 1), (0, 3), (-1, 1), (0, 1), (1, 1), (0, 3), (-1, 1), (-1, 1), (1, 0), (0, 1)]

def is_monster_here(raster, y, x):
    start = raster[y][x]
    if not start == '#':
        return False
    for move in monster_path:
        y = y + move[0]
        x = x + move[1]
        try:
            if not raster[y][x] == '#':
                return False
        except IndexError:
            return False
    return True 


def show_monster(raster, y, x):
    l = list(raster[y])
    l[x] = '▓'
    raster[y] = "".join(l)
    for move in monster_path:
        y = y + move[0]
        x = x + move[1]
        l = list(raster[y])
        l[x] = '▓'
        raster[y] = "".join(l)

def find_monsters_in_raster(raster):
    monster_count = 0
    for y, line in enumerate(raster):
        for x, c in enumerate(line):
            monster = is_monster_here(raster, y, x)
            if monster:
                monster_count += 1
                show_monster(raster, y, x)
    return monster_count

def find_monsters(raster):
    for i in range(4):
        monster_count = find_monsters_in_raster(raster)
        if monster_count == 0:
            print("rotating raster...")
            raster = rotate(raster)
        else:
            return raster

    monster_count = find_monsters_in_raster(raster)
    if monster_count == 0:
        print("flipping raster...")
        raster = flip_hor(raster)
    else:
        return raster

    for i in range(4):
        monster_count = find_monsters_in_raster(raster)
        if monster_count == 0:
            print("rotating raster...")
            raster = rotate(raster)
        else:
            return raster

    return raster


raster = find_monsters(raster)
print_raster(raster)

final_count = 0
for y, line in enumerate(raster):
    for x, c in enumerate(line):
        if c == '#':
            final_count += 1

print(final_count)