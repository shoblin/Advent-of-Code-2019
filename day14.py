#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     25.01.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import math

def needs_list(chemical, needs):
    '''
    '''
    chemical_name = chemical['chemical']
    if chemical['chemical']  not in needs:
        needs[chemical['chemical']] = chemical['amount']
    else:
        needs[chemical['chemical']] += chemical['amount']


def count_ore(output_chemical, output_amount, task_list, needs):
    '''
    Count ores
    '''
    ores = 0

    if output_chemical == "ORE":
        return output_amount

    if output_chemical not in needs:
        needs[output_chemical] = 0

    output_amount -= needs[output_chemical]
    produced = task_list[output_chemical][0]
    k = math.ceil(output_amount/produced)
    needs[output_chemical] = k * produced - output_amount

    for n_element, element in task_list[output_chemical][1]:
        ores += count_ore(element, n_element * k, task_list, needs)

    return ores

def parse(x):
    n, ingredient = x.split(' ')
    return int(n), ingredient

def read_input_values(file_name, num_row = 0):
    '''
    Read values from file and input its into dict = {out_int}
    '''
    task_dict = {}
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
    for line in lines:
        inputs, outputs  = line.split(' => ')
        n_out, out_element = parse(outputs)
        task_dict[out_element] = (n_out, [parse(elem.strip()) for elem in inputs.split(',')])

    return task_dict

def main():
    # Part 1: Find number of ORE for create 1 FUEL
    task_dict = read_input_values('day14_puzzle_input.txt')
##    task_dict = read_input_values('day14_puzzle_input_test.txt')
    need_chemicals = {}
##    print(task_dict)
##    need_chemicals = {'FUEL': 1}
    result = count_ore('FUEL', 1, task_dict, need_chemicals)
    print(result)


    hi = int(1e12)
    need_chems = {}
    lo = hi//count_ore('FUEL', 1, task_dict, need_chems)
    while hi > lo:
        mid = lo+(hi-lo)//2 + 1
        surplus = {}
        cost = count_ore('FUEL', mid, task_dict, surplus)
        # print(cost)
        if cost < int(1e12):
            lo = mid
        else:
            hi = mid-1

    print('Part 2: ', lo)




if __name__ == '__main__':
    main()
