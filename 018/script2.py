import itertools
import re

# test: n/a
# input: 231235959382961

lines = open('input.txt', 'r').read().splitlines()
lines = list(map(lambda l: l.replace(' ', ''), lines))


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


def solve(equation):
    sub_equations = extract_parenthesis(equation)

    for se in sub_equations:
        result = solve(se)
        equation = equation.replace(f"({se})", str(result), 1)

    while True:
        if equation.count('+') == 0:
            break
        all_additions = re.findall('\d+\+\d+', equation)
        add = all_additions[0]
        addition_result = eval(add)
        equation = equation.replace(add, str(addition_result), 1)
    return eval(equation)


print(sum(map(solve, lines)))
