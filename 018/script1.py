import itertools
import re

# test: n/a
# input: 8929569623593

lines = open('input.txt', 'r').read().splitlines()
lines = list(map(lambda l: l.replace(' ', ''), lines))


def extract_parenthesis(line):
    tiles = []
    start_idx = None
    open_count = 0
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


def solve(equation):
    sub_equations = extract_parenthesis(equation)

    for se in sub_equations:
        result = solve(se)
        equation = equation.replace(f"({se})", str(result), 1)

    while (equation.count('*') != 0 and equation.count('+') != 0):
        tile = re.search("\d+(\*|\+)\d+", equation).group(0)
        equation = str(eval(tile)) + equation[len(tile):]

    return eval(equation)


print(sum(map(solve, lines)))
