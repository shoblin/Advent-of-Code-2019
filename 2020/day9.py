#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     07.01.2021
# Copyright:   (c) atopolskiy 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from collections import deque
def read_file(filename):
    data = []
    with open(filename, 'r') as fl:
        for line in fl:
            data.append(int(line))

    return data

def check_number(number, preamble_list):
    ''' '''
    len_list = len(preamble_list)
    add_result = []
    for i in range(len_list):
        for j in range(i+1,len_list):
            add_result.append(preamble_list[i] + preamble_list[j])

    return number in add_result

##    return number in add_result


def find_bug_number(data, num_preamble = 25):
    '''
    Find number that does not follow this rule
    '''
    for curr_pos in range(num_preamble, len(data)):
        start_pos, end_pos = curr_pos - num_preamble, curr_pos

        if not check_number(data[curr_pos], data[start_pos:end_pos]):
            return data[curr_pos]


def solution2(data, target_weakness):
    ''' '''
    for num in range(2, len(data)):
        for pos in range(len(data) - num + 1):
            if sum(data[pos:pos+num]) == target_weakness:
                print(min(data[pos:pos+num]) + max(data[pos:pos+num]))

def main():
    data = read_file('data/day9_puzzle_input.txt')
##    print(data)
    target_weakness = find_bug_number(data)
    print (target_weakness)
    solution2(data, target_weakness)


if __name__ == '__main__':
    main()
