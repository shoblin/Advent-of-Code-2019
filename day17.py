#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     23.02.2020
# Copyright:   (c) Shoblin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lib.intcode import Computer
import lib.functions_au as fa

def create_map(optcode):
    '''
    '''
    map_codes = []
    line_code = []

    computer = Computer(optcode)
    while not computer.done:
        computer.calculate()
        if not computer.done:

            if computer.output == 10:
                if len(line_code) != 0:
                    map_codes.append(line_code[:])
                line_code =[]

            else:
                line_code.append(computer.output)

    return map_codes

def draw_map(map_code):
    '''
    35 - #,
    46 - .,
    10 - starts a new line
    '''

    for line in map_code:
        str_line = ''
        for ch in line:
            str_line += chr(ch)

        print(str_line)

def cross_check(map_code, x, y):
    '''
    '''
    #cross coordinates
    cross = [(0,1), (1,0), (0,-1), (-1,0)]

    for cr in cross:
        check_x = x + cr[0]
        check_y = y + cr[1]

        if map_code[check_y][check_x] != 35:
            return False

    return True



def calculate_coordinates(map_code):
    '''
    '''
    # Find max X and Y for cycles
    max_y = len(map_code) - 1
    max_x = len(map_code[0]) - 1

    coords = []
    result = 0

    for y in range(1, max_y):
        for x in range(1, max_x):
            if map_code[y][x] == 35 and cross_check(map_code, x, y):
                coords.append((x,y))

    for coord in coords:
        result += coord[0] * coord[1]

    print(result)


def main():
    #Take optcode from file
    opcode_list = fa.read_input_values('day17_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]

    task_map_code = create_map(opcode_list)
    draw_map(task_map_code)

    calculate_coordinates(task_map_code)







if __name__ == '__main__':
    main()
