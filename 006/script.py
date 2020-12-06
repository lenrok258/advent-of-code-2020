from string import ascii_lowercase

lines = open('input.txt', 'r').read().splitlines()

count = 0
prv_group = set(ascii_lowercase)
for line in lines:

    if not len(line):
        count += len(prv_group)
        prv_group = set(ascii_lowercase)
        continue

    prv_group = prv_group.intersection(line)

print(count)


