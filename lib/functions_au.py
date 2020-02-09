#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     07.12.2019
# Copyright:   (c) atopolskiy 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os



def read_input_values(file_name, num_row = 0):
    '''
    Read values from file and input its into list
    '''
    dir = os.path.abspath(os.curdir)
    full_name = dir + '\\' + file_name
    with open(full_name, "r") as file:
        line = file.read().splitlines()
        list = line[num_row].split(',')

    return list

def reed_maps(file_name):
    '''
    Read values from file and input its into list[list]
    '''
    result_list = []
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
    for line in lines:
        symb_list = []
        for symb in line:
            symb_list.append(symb)

        result_list.append(symb_list)

    return result_list









