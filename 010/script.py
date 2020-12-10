import itertools
import cProfile

# test 1: 8
# test 2: 19208
# final: 386869246296064

numbers = list(map(int, open('input.txt', 'r').read().splitlines()))
numbers.sort()
device_j = numbers[-1] + 3
numbers.append(device_j)

numbers.append(0)
numbers.sort()

cache = dict()


def remove_chargers(numbers):

    cache_key = frozenset(numbers)

    if cache_key in cache:
        return cache[cache_key]

    count_success = 0

    for i, number in enumerate(numbers[1:], start=1):

        # device
        if i == len(numbers) - 1:
            cache[cache_key] = count_success
            return count_success

        if numbers[i + 1] - numbers[i - 1] <= 3:
            n_copy = numbers.copy()
            n_copy.remove(number)
            count_success += remove_chargers(n_copy[i-1:]) + 1


cProfile.run('remove_chargers(numbers)')
results = remove_chargers(numbers)

print(results + 1)
