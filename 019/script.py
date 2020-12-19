import re

# test1: 2
# test2: 12
# input1: 142
# input2: 294

blocks = open('input2.txt', 'r').read().split("\n\n")
rules = {l[0]:l[1].replace('"', '') for l in map(lambda l : l.split(": "), blocks[0].splitlines())}
messages = blocks[1].splitlines()

def build_regex(rule, depth = 0):
    # break loops
    if depth > 100:
        return '' 

    if re.match('[a-z]', rule):
        return rule
    
    for n in rule.split(' '):
        if re.match('\d+', n):
            depth += 1
            tile_regex = build_regex(rules[n], depth)
            rule = rule.replace(n, tile_regex, 1)

    return f"({rule})"

regex = f"^{build_regex(rules['0'])}$".replace(' ', '')
result = sum(map(lambda m: 1 if re.match(regex, m) else 0, messages))
print(result)