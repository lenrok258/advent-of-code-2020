from string import ascii_lowercase

def count_outer_bags(color):
    lines = open('input.txt', 'r').read().splitlines()
    outer_colors = set()
    for line in lines:
        outer_inner = line.split(" bags contain ")
        outer = outer_inner[0]
        inner = outer_inner[1]
        if color in inner:
            outer_colors.add(outer)
            outer_colors.update(count_outer_bags(outer))
    return outer_colors


outer_colors = count_outer_bags("shiny gold")

print(outer_colors)

print(len(outer_colors))


