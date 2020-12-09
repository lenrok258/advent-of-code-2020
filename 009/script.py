import itertools as itool


def find_black_sheep(numbers, preamble_size):
    for i, number in enumerate(numbers[preamble_size:], start=preamble_size):
        candidates = numbers[(i - preamble_size):i]
        sums = map(sum, itool.combinations(candidates, 2))
        if not number in sums:
            return number


def find_black_sheep_ingredients(numbers, black_sheep):
    for i, number in enumerate(numbers):
        sums = list(itool.accumulate(numbers[i:]))
        if black_sheep in sums:
            j = sums.index(black_sheep)
            return numbers[i:(i + j + 1)]


lines = map(int, open('input.txt', 'r').read().splitlines())
numbers = list(map(int, lines))

# star 1
black_sheep = find_black_sheep(numbers, 25)
print(f"░░░ Black sheep (🐑): \t{black_sheep}")  # 57195069

# star 2
ingredients = find_black_sheep_ingredients(numbers, black_sheep)
ingredients.sort()
print(f"░░░ Weakness: \t\t{ingredients[0] + ingredients[-1]}")  # 7409241
