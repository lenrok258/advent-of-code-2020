import itertools

# test 1: 8
# test 2: 19208

numbers = list(map(int, open('input_test2.txt', 'r').read().splitlines()))
numbers_input_len = len(numbers)
numbers.sort()
device_j = numbers[-1] + 3
numbers.append(device_j)

numbers.append(0)
numbers.sort()

print(numbers)

def remove_charger(numbers):

    count_success = 0
    
    for i, number in enumerate(numbers[1:], start=1):

        # if len(numbers) < (numbers_input_len * 0.3):
        #     return list()

        # device
        if i == len(numbers) - 1:
            # print("returning restult")
            return count_success

        # print("{} {}".format(i, number))
        if numbers[i+1] - numbers[i-1] <= 3:
            # print("{} {}".format(len(numbers), numbers))
            # print("remove: {}".format(number))
            n_copy = numbers.copy()
            n_copy.remove(number)
            count_success += 1
            count_success += remove_charger(n_copy[i-1:])


results = remove_charger(numbers)
# results.sort()

# results = list(k for k, _ in itertools.groupby(results))

print("=========")

# for i in results:
#     print("{} {}".format(len(i), i))

print(results + 1)


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
