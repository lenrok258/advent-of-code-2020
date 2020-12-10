import itertools
import cProfile

# test 1: 8
# test 2: 19208

numbers = list(map(int, open('input.txt', 'r').read().splitlines()))
numbers_input_len = len(numbers)
numbers.sort()
device_j = numbers[-1] + 3
numbers.append(device_j)

numbers.append(0)
numbers.sort()

print(numbers)

def print_with_depth(msg, depth):
    left_margin = " " * depth
    print(left_margin + msg)

cache=dict()
def remove_charger(numbers):

    cache_key = frozenset(numbers)

    if cache_key in cache:
        return cache[cache_key]

    count_success = 0
    
    for i, number in enumerate(numbers[1:], start=1):

        # device
        if i == len(numbers) - 1:
            # print("returning restult")
            cache[cache_key] = count_success
            return count_success

        # print("{} {}".format(i, number))
        if numbers[i+1] - numbers[i-1] <= 3:
            # print("{} {}".format(len(numbers), numbers))
            # print("remove: {}".format(number))
            n_copy = numbers.copy()
            n_copy.remove(number)
            count_success += 1
            count_success += remove_charger(n_copy[i-1:])

def remove_charger_fast(start_idx, last_left, depth):

    count_success = 0
    
    # for i, number in enumerate(numbers[start_idx:], start=start_idx):

    for i in range(start_idx, len(numbers)):

        number = numbers[i]
        # if len(numbers) < (numbers_input_len * 0.3):
        #     return list()

        # device
        if i == len(numbers) - 1:
            # print("returning restult")
            return count_success

        print_with_depth("d:{}\t i:{}\tn:{}\tll:{}".format(depth, i, number, last_left), depth)

        if numbers[i+1] - last_left <= 3:
            # print("{} {}".format(len(numbers), numbers))
            print_with_depth("remove: {} ({}-{})".format(number, numbers[i+1], last_left), depth)
            # n_copy = numbers.copy()
            # n_copy.remove(number)
            count_success += 1
            count_success += remove_charger_fast(i + 1, last_left, depth+1)
        else:
            last_left = number

def remove_charger_fast2(in_numbers):

    count_success = 0

    singles = list()
    for i, number in enumerate(in_numbers[1:], start=1):

        # device
        if i == len(in_numbers) - 1:
            break

        if in_numbers[i+1] - in_numbers[i-1] <= 3:
            singles.append(i)
    
    print(singles)
    print(len(singles))

    combinations = list()
    for i in range(2, len(singles) + 1):
        combinations.extend(itertools.combinations(singles, i))
    
    # print(combinations)

    return len(combinations) + len(singles) + 1

    
def compute_final(nums):

    total = 1

    for i, number in enumerate(nums):
        pass




# results = remove_charger(numbers)
cProfile.run('remove_charger(numbers)')

# results = remove_charger_fast(1, 0, 0)
# cProfile.run('remove_charger_fast(1, 0)')

# results = remove_charger_fast2(numbers)
# cProfile.run('remove_charger_fast2(numbers)')

print(results + 1)
print(len(cache))

# results.sort()

# results = list(k for k, _ in itertools.groupby(results))

# for i in results:
#     print("{} {}".format(len(i), i))




# 35
# one = 0
# three = 0
# prv = 0

# for number in numbers:
#     delta = number - prv
#     print("{} {}".format(number, delta))

#     if delta == 1:
#         one += 1
#     elif delta == 3:
#         three += 1
#     prv = number


# print(one)
# print(three)

# print(one*three)
