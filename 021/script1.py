import pprint
import copy
import functools
import operator

pp = pprint.PrettyPrinter(indent=2)

# test: 5
# input: 

lines = open('input.txt', 'r').read().splitlines()

data = []
all_ingredients = []
for line in lines:
    tiles = line.replace(')', '').split(' (contains ')
    ingredients = tiles[0].split(' ')
    alergens = tiles[1].split(', ')
    data.append((ingredients, alergens))
    all_ingredients.extend(ingredients)

all_ingredients = set(all_ingredients)

# pp.pprint(data)
# print()

mappings = {}

for ingredients, alergens in data:
    for a in alergens:
        if a not in mappings:
            mappings[a] = ingredients
        else:
            mappings[a] = list(set(mappings[a]).intersection(set(ingredients)))

# pp.pprint(mappings)
# print()

final_mappings = copy.deepcopy(mappings)

while True:
    key_with_one_ingr = None
    for alergen, ingredients in mappings.items():
        if len(ingredients) == 1:
            key_with_one_ingr = (alergen, ingredients)
            del mappings[key_with_one_ingr[0]]
            break

    if not key_with_one_ingr:
        break

    for k, v in final_mappings.items():
        if k == key_with_one_ingr[0]:
            continue
        if key_with_one_ingr[1][0] in v:
            v.remove(key_with_one_ingr[1][0])
            mappings[k].remove(key_with_one_ingr[1][0])

    key_with_one_ingr = None

pp.pprint(final_mappings)

ingr_with_al = set(functools.reduce(operator.iconcat, final_mappings.values(), []))
print(ingr_with_al)
print(all_ingredients)

ingr_with_no_al = all_ingredients - ingr_with_al

print(ingr_with_no_al)

final_count = 0
for ingredients, alergens in data:
    for i in ingredients:
        if i in ingr_with_no_al:
            final_count += 1

print(final_count)

# --------------------
# -------------------- STAR 2
# --------------------

ingr = list(final_mappings.keys())
ingr.sort()
alerg = list(map(lambda i: final_mappings[i][0], ingr))
print(",".join(alerg))