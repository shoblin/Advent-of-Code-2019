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
import lib.functions_au as fa

def find_pair(data_list):
    '''
    Find pair with sum = 2020
    '''
    first_num, second_num = 0, len(data_list) - 1
    curr_num = first_num

    while True:
        sum_num = data_list[curr_num] + data_list[second_num]
        if sum_num > 2020:
            second_num -= 1
            curr_num = first_num
        elif sum_num < 2020:
            curr_num += 1
        else:
            print("mult =", data_list[curr_num] * data_list[second_num],'sum =', sum_num)
            break

def find_three(data_list):
    '''
    Find three numbers with sum = 2020
    '''
    first_num, second_num = 0, len(data_list) - 1
    curr_num = first_num

    while True:
        sum_num1 = data_list[curr_num] + data_list[second_num]
        if sum_num1 >= 2020:
            second_num -= 1
            curr_num = first_num
        elif sum_num1 < 2020:
            for third_num in range(curr_num + 1, second_num):
                sum_num = sum_num1 + data_list[third_num]
                if sum_num >2020:
                    break
                if sum_num == 2020:
                    print("mult =", data_list[curr_num] * data_list[second_num]* data_list[third_num],'sum =', sum_num)
                    return

            curr_num += 1


def main():
    data_list1 = fa.read_file_col('data/day1_puzzle_input.txt')
    data_list1.sort()

    find_three(data_list1)



if __name__ == '__main__':
    main()
