import itertools
import re

# test: n/a
# input - star 1: 8929569623593
# input - star 2: 231235959382961


def extract_parenthesis(line):
    tiles, start_idx, open_count = [], None, 0
    for i, c in enumerate(line):
        if c == '(':
            open_count += 1
            if start_idx == None:
                start_idx = i
        if c == ')':
            open_count -= 1
            if open_count == 0:
                tiles.append(line[start_idx + 1:i])
                start_idx = None
    return tiles


def solve_1(equation):
    for se in extract_parenthesis(equation):
        equation = equation.replace(f"({se})", str(solve_1(se)), 1)

    while (equation.count('*') != 0 and equation.count('+') != 0):
        tile = re.search("\d+(\*|\+)\d+", equation).group(0)
        equation = str(eval(tile)) + equation[len(tile):]

    return eval(equation)


def solve_2(equation):
    for se in extract_parenthesis(equation):
        equation = equation.replace(f"({se})", str(solve_2(se)), 1)

    while not equation.count('+') == 0:
        addition = re.findall('\d+\+\d+', equation)[0]
        equation = equation.replace(addition, str(eval(addition)), 1)

    return eval(equation)


lines = open('input.txt', 'r').read().splitlines()
lines = list(map(lambda l: l.replace(' ', ''), lines))

print(sum(map(solve_1, lines)))
print(sum(map(solve_2, lines)))
