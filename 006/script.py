import string

input_file = open('input.txt', 'r')
lines = input_file.readlines()


def full_group():
    return list(string.ascii_lowercase)


count = 0
prv_group = full_group()
current_group = list()
for line in lines:
    line = line.replace('\n', '')

    if len(line) == 0:
        current_group = list(set(current_group))
        count += len(current_group)
        prv_group = full_group()
        current_group.clear()
        continue

    line_chars = list(line)
    current_group = list(set(prv_group).intersection(line_chars))
    prv_group = current_group

print("\n░░░░░░░░░░░░░░░░░░░\n░░░ Answer {} ░░░\n░░░░░░░░░░░░░░░░░░░".format(count))
