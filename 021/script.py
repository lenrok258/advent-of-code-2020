import copy
import functools
import operator

# test star 1: 5
# input star 1: 2786
# test star 2: mxmxvkd,sqjhc,fvjkl
# input star 2: prxmdlz,ncjv,knprxg,lxjtns,vzzz,clg,cxfz,qdfpq

lines = open('input.txt', 'r').read().splitlines()

data, all_ingredients = [], []
for line in lines:
    tiles = line.replace(')', '').split(' (contains ')
    ingredients = tiles[0].split(' ')
    alergens = tiles[1].split(', ')
    data.append((ingredients, alergens))
    all_ingredients.extend(ingredients)

all_ingr = set(all_ingredients)

mappings = {}

for ingredients, alergens in data:
    for a in alergens:
        if a not in mappings:
            mappings[a] = ingredients
        else:
            mappings[a] = list(set(mappings[a]).intersection(set(ingredients)))

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

ingr_with_al = set(functools.reduce(operator.iconcat, final_mappings.values(), []))
ingr_with_no_al = all_ingr - ingr_with_al

all_ingr_with_dup = list(functools.reduce(operator.iconcat, map(lambda d : d[0], data), []))
print(sum(map(lambda a: 1 if a in ingr_with_no_al else 0, all_ingr_with_dup)))

#  STAR 2
ingr = list(final_mappings.keys())
ingr.sort()
print(",".join(list(map(lambda i: final_mappings[i][0], ingr))))