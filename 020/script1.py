

# test: 20899048083289
# input: 5775714912743

# BLOCK_WIDTH = 10

blocks = open('input_test.txt', 'r').read().split("\n\n")

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

def extract_edges(img_idx):
    # print(img_idx)
    edges = []
    data = imgs_data[img_idx]
    edges.append(data[0]) # top
    left, right = "", ""
    for line in data:
        left += line[0]
        right += line[-1]
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
        print(img_id)
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





corners_ids = []
result = 1
for i, img_idx in enumerate(imgs_ids):
    print(f"{i} {img_idx} {is_corner(i)}")
    if is_corner(i):
        corners_ids.append(imgs_ids[i])
        result *= int(imgs_ids[i])

print(corners_ids)
print(result)

