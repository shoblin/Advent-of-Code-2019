#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     14.02.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def transform_task(task):
    return [int(x) for x in task]

def creat_pattern(pattern, repeats):
    '''

    '''
    result = []
    for pat in pattern:
        result += [pat] * repeats
    return result


def fft(task_str, num_phases):
    '''

    '''
    task_list = transform_task(task_str)
    num_str = len(task_list)
    pattern = [0, 1, 0, -1]
    result = []

    for phase in range(1, num_phases + 1):
##        calulate creat_pattern(pattern, phase))

def main():
    task_test1 = '12345678'
    task_test2 = '80871224585914546619083218645595'

    t = fft(task_test1, 4)


if __name__ == '__main__':
    main()
