
input_file = open('input.txt', 'r')
lines = input_file.readlines()

number_of_correct = 0

# excercise 1:

# for password_line in lines:
#     policy_touple = password_line.split(":")
#     policy = policy_touple[0]
#     password = policy_touple[1].strip()
#     min_occurences = int(policy.split(" ")[0].split("-")[0])
#     max_occurences = int(policy.split(" ")[0].split("-")[1])
#     letter = policy.split(" ")[1]

#     number_of_occurences = password.count(letter)

#     print("debug {} {} {} {}".format(
#         min_occurences, max_occurences, letter, password))

#     if (number_of_occurences >= min_occurences and number_of_occurences <= max_occurences):
#         print("correct pass: {}".format(password))
#         number_of_correct += 1


# print("answer {}".format(number_of_correct))

print("----------------------------------------------")

# excercise 2:

real_number_of_correct = 0

for password_line in lines:
    policy_touple = password_line.split(":")
    policy = policy_touple[0]
    password = policy_touple[1].strip()
    occurence1 = int(policy.split(" ")[0].split("-")[0])
    occurence2 = int(policy.split(" ")[0].split("-")[1])
    letter = policy.split(" ")[1]

    if (password[occurence1 - 1] is letter) != (password[occurence2 - 1] is letter): # beautiful XOR!
        print("{} {} {}".format(password, letter, occurence1))
        real_number_of_correct += 1


print("answer {}".format(real_number_of_correct)) 
