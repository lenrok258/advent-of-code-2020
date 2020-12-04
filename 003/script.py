
def compute_trees(move_horizontal, move_vertical):

    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    trees = 0

    position_x = 0
    position_y = move_vertical

    for line in lines[position_y:]:

        if position_y % move_vertical != 0:
            position_y += 1
            continue

        line = line.replace('\n', '')

        position_x += move_horizontal

        if position_x >= len(line):
            position_x = position_x - len(line)

        position_content = line[position_x]
        if position_content is '#':
            trees += 1

        print(line.replace("\n", ''))
        print(("-" * position_x) + "^")
        print("position:{}, trees:{}\n".format(position_x, trees))

        position_y += 1

    return trees

# part 1:
# trees = compute_trees(3, 1)
# print("number_of_trees: {}".format(trees))


# part 2:
trees1_1 = compute_trees(1, 1)
trees3_1 = compute_trees(3, 1)
trees5_1 = compute_trees(5, 1)
trees7_1 = compute_trees(7, 1)
trees1_2 = compute_trees(1, 2)

answer2 = trees1_1 * trees3_1 * trees5_1 * trees7_1 * trees1_2

print("trees multiplication:{}".format(answer2))
