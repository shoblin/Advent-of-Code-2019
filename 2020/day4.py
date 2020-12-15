#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     09.12.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def creat_data_list(filename):
    '''
    Take data from file and create list with dicts
    '''
    passports = []

    with open(filename, "r") as file:
        curr_passport = ''
        for line in file:
            line = line.strip()
            if line:
                curr_passport += line + ' '
            else:
                passports.append(curr_passport)
                curr_passport = ''

    i = 0
    for passport in passports:
        fields = passport.split()
        dict ={field.split(':')[0]: field.split(':')[1] for field in fields}
        passports[i] = dict
        i +=1

    return passports

def check_fields(passport, nec_fields):
    '''
    Check passport and detecting which passports have all required fields
    '''
    for field in nec_fields:
        if len(passport) == 8:
            return True
        if field not in passport:
            return False
    return True

def check_height(height):
    '''
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    '''

    if not height.endswith('cm') and not height.endswith('in'):
        return False

    hgt = int(height[:-2])
    if height.endswith('cm') and (hgt < 150 or hgt > 193):
        return False
    if height.endswith('in') and (hgt < 59 or hgt > 76):
        return False

    return True


def check_hair_color(hcl):
    '''
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
    '''
    allowed_symbs = 'abcdef0123456789'
    if not hcl.startswith('#') or len(hcl) != 7:
        return False
    for sym in hcl[1:]:
        if not sym in allowed_symbs:
            return False

    return True

def check_eye_color(ecl):
    '''
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    '''
    allow_ecl = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if not ecl in allow_ecl:
        return False

    return True


def check_pid(pid):
    '''
    '''
    digit ='0123456789'
    if len(pid) != 9:
        return False
    for dig in pid:
        if not dig in digit:
            return False

    return True


def check_passport(passport):
    '''
    === Passport Fields: ===
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''
    byr = (1920, 2002)              ## byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr = (2010, 2020)              ## iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr = (2020, 2030)              ## eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

    try:
        # Check byr (Birth Year)
        if int(passport['byr']) < byr[0] or int(passport['byr']) > byr[1]:
            return False

        # Check iyr (Issue Year)
        if int(passport['iyr']) < iyr[0] or int(passport['iyr']) > iyr[1]:
            return False

        # Check eyr (Expiration Year)
        if int(passport['eyr']) < eyr[0] or int(passport['eyr']) > eyr[1]:
            return False

        # Check hgt (Height)
        if not check_height(passport['hgt']):
            return False

        # Check hair color
        if not check_hair_color(passport['hcl']):
            return False

        if not check_eye_color(passport['ecl']):
            return False

        if not check_pid(passport['pid']):
            return False

        return True

    except KeyError:
        return False


def main():

    necessary_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = creat_data_list('data/day4_puzzle_input.txt')

    num_good_passports = 0

    print('=== First task ===')
    for passport in passports:
        if check_fields(passport, necessary_fields):
            num_good_passports +=1

    print('Result:',num_good_passports)

    validate_passports = 0
    print('=== Second task ===')
    for passport in passports:
        if check_passport(passport):
            validate_passports +=1

            print(passport)

    print('Result:', validate_passports)


if __name__ == '__main__':
    main()
