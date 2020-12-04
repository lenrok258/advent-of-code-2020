
input_file = open('input.txt', 'r')
lines = input_file.readlines()

input_numbers = list(map(lambda line: int(line), lines))

# print(input_numbers)

for i in input_numbers:
    for j in input_numbers:
        if i + j == 2020:
            print("Para: {} {}", i, j)
            print("Wynik mnożenia: {}", i * j)

print("------------------------------")

for i in input_numbers:
    for j in input_numbers:
        for k in input_numbers:
            if i + j + k == 2020:
                print("Liczby: {} {} {}", i, j, k)
                print("Wynik mnożenia: {}", i * j * k)
