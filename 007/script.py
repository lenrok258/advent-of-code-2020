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

def count_inner_bags(color):
    lines = open('input.txt', 'r').read().splitlines()
    counter = 0 
    for line in lines:
        outer_inner = line.split(" bags contain ")
        outer = outer_inner[0]
        inner = outer_inner[1].replace('.', '').replace(' bags', '').replace(' bag', '')

        if color in outer:
            if "no other bags" in line:
                return 0
            inners = inner.split(", ")
            for i in inners:
                i_array = i.split(" ", 1)
                counter += int(i_array[0])
                counter += int(i_array[0]) * count_inner_bags(i_array[1])
    return counter

print(len(count_outer_bags("shiny gold")))
print(count_inner_bags("shiny gold"))