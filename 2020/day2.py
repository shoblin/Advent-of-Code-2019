#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     07.12.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def prepare_line(line):
    '''
    Split line
    '''
    policy, password = line.split(':')
    l_num, letter = policy.split()
    first_num, second_num = l_num.split('-')
    password = password.strip()

##    print(first_num,"|",second_num,"|", letter,"|",password,"|", len(password))

    return int(first_num), int(second_num), letter, password

def check_pass1(min_l, max_l, letter, password):
    '''
    check passwords
    '''
    num_letters = password.count(letter)
    if num_letters >= int(min_l) and num_letters <= int(max_l):
        return True
    return False

def check_pass2(first_num, second_num, letter, password):
    '''
    Splite line and check passwords
    '''

    if password[first_num] == letter and password[second_num] != letter:
        return True
    if password[first_num] != letter and password[second_num] == letter:
        return True
    return False


def main():
    num_gpass1 = 0
    num_gpass2 = 0
    with open("data/day2_puzzle_input.txt", "r") as file:
        for line in file:
            min_num, max_num, letter, password = prepare_line(line)

            if check_pass1(min_num, max_num, letter, password):
                num_gpass1 +=1
            if check_pass2(min_num - 1, max_num - 1, letter, password):
                num_gpass2 +=1

    print(num_gpass1, num_gpass2)

if __name__ == '__main__':
    main()
