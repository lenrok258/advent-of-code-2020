input_file = open('input.txt', 'r')
lines = input_file.readlines()

trees = 0

position_index = 0
for line in lines[1:]:
    line = line.replace('\n', '') 

    position_index += 3

    if position_index >= len(line):
        position_index = position_index - len(line)

    position_content = line[position_index]
    if position_content is '#':
        trees += 1

    print(line.replace("\n", ''))
    print(("-" * position_index) + "^")
    print("position:{}, trees:{}\n".format(position_index, trees))

print("number_of_trees: {}".format(trees))
