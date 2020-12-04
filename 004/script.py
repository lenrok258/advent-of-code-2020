input_file = open('input.txt', 'r')
lines = input_file.readlines()

valid_count = 0


def isPassportLineValid(passportLine):
    if 'byr' in passportLine \
            and 'iyr' in passportLine \
            and 'eyr' in passportLine \
            and 'hgt' in passportLine \
            and 'hcl' in passportLine \
            and 'ecl' in passportLine \
            and 'pid' in passportLine:
        return True
    return False


current_passport = ''
for line in lines:

    if line is "\n":
        # validate
        if isPassportLineValid(current_passport):
            valid_count += 1
            print(current_passport)
        current_passport = ''
        continue

    current_passport += line.replace('\n', '') + " "

print("answer1: {}".format(valid_count))
