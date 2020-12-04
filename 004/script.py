import re

input_file = open('input.txt', 'r')
lines = input_file.readlines()

valid_count = 0


def isValidHairColor(color):
    if not re.match("^#[0-9a-f]{6}$", color):
        return False
    return True


def isValidHeight(height):
    unit = height[len(height)-2:]
    if not (unit == 'cm' or unit == 'in'):
        return False

    value = height[:len(height)-2]
    if not value.isnumeric():
        return False

    value = int(value)

    if unit == 'cm':
        if value < 150 or value > 193:
            return False

    if unit == 'in':
        if value < 59 or value > 76:
            return False

    return True


def isValidNumber(input, min, max):
    if not input.isnumeric() or not len(input) == 4:
        return False
    if int(input) < min or int(input) > max:
        return False
    return True


def areRequiredFieldsPresent(passportLine):
    if 'byr' in passportLine \
            and 'iyr' in passportLine \
            and 'eyr' in passportLine \
            and 'hgt' in passportLine \
            and 'hcl' in passportLine \
            and 'ecl' in passportLine \
            and 'pid' in passportLine:
        return True
    return False


def areValuesValid(passportDict):
    byr = passportDict.get('byr')
    if not isValidNumber(byr, 1920, 2002):
        return False

    iyr = passportDict.get('iyr')
    if not isValidNumber(iyr, 2010, 2020):
        return False

    eyr = passportDict.get('eyr')
    if not isValidNumber(eyr, 2020, 2030):
        return False

    hgt = passportDict.get('hgt')
    if not isValidHeight(hgt):
        return False

    hcl = passportDict.get('hcl')
    if not isValidHairColor(hcl):
        return False

    ecl = passportDict.get('ecl')
    if not (ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'):
        return False

    pid = passportDict.get('pid')
    if not pid.isnumeric() or not len(pid) == 9:
        return False

    return True


current_passport = ''
for line in lines:
    line = line.replace('\n', '')

    if len(line) == 0:
        # validate
        current_passport = current_passport.strip()
        if areRequiredFieldsPresent(current_passport):

            fieldsDict = dict(x.split(":")
                              for x in current_passport.split(" "))

            if areValuesValid(fieldsDict):  # star 2 only
                valid_count += 1
                print(current_passport + "\n")

        current_passport = ''
        continue

    current_passport += line + " "

print("answer: {}".format(valid_count))
