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
import lib.functions_au as fa

def transform_task(task):
    return [int(x) for x in task]

def creat_pattern(pattern, repeats):
    '''
    Calculate parttern for new_step
    '''
    result = []
    for pat in pattern:
        result += [pat] * repeats
    return result
def calculate_number(input_list, new_pattern):
    '''
    '''
    point = 1
    result = 0
    for curr_num in input_list:
        if point >= len(new_pattern):
            point = 0
        result += curr_num * new_pattern[point]
        point += 1
    return abs(result) % 10


def calculate_phase(input_list):
    '''
    Calculate output for all symbols
    '''
    pattern = [0, 1, 0, -1]
    result = []

    for num in range(1,len(input_list)+1):
        new_pattern = creat_pattern(pattern, num)
        result.append(calculate_number(input_list, new_pattern))

    return result


def fft(task_str, num_phases):
    '''

    '''
    task_list = transform_task(task_str)

    for phase in range(1, num_phases + 1):
        task_list = calculate_phase(task_list)

    return task_list[:8]

def main():
    task_test1 = '12345678'
    task_test2 = list('03036732577212944063491565474664')

    task = fa.read_input_values('day16_puzzle_input.txt')

    t = fft(task[0], 100)
    result = ''.join(map(str, t))
    print('Part1:', result)

    task = task[0] * 10000
    offset = int(''.join([str(d) for d in task[:7]]))

    task_list = task[offset:]
    task_list =[int(x) for x in task_list]

    for iteration in range(100):
        restsum = sum(task_list)
        for i, n in enumerate(task_list):
            task_list[i] = abs(restsum) % 10
            restsum -= n
    result = ''.join(str(n) for n in task_list[:8])

    print('Part 2: ',  result)



if __name__ == '__main__':
    main()
