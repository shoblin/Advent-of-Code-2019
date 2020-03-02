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

### Part1: To calibrate the cameras by getting the alignment parameters of some
### well-defined points.


def cross_check(map_code, x, y):
    '''
    Part 1: Find coordinates of crossing lines.
    Return True if find line crossing
    Return False if don't find line crossing
    '''
    #cross coordinates
    cross = [(0,1), (1,0), (0,-1), (-1,0)]

    for cr in cross:
        check_x = x + cr[0]
        check_y = y + cr[1]

        if map_code[check_y][check_x] != 35:
            return False

    return True


def calculate_result_part1(map_code):
    '''
    Part1: Calculate results SUM of multiplication of X and Y
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

    return result


def create_map(optcode):
    '''
    Create map: calculate map. Divide into lines, 10 - starts a new line
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
    Draw map and find coordinates of robot
    35 - #,
    46 - .,
    10 - starts a new line
    '''
    bot_x, bot_y = 0, 0
    y = 0

    for line in map_code:
        str_line = ''
        x = 0
        for ch in line:
            str_line += chr(ch)
            # Find symbol '^' and remember coordinates
            if ch == 94:
                bot_x, bot_y = x, y
            x += 1
        y += 1
        print(str_line)
    return bot_x, bot_y


def calculate_path(map_code, bot_x, bot_y):
    '''
    Calculate Bot's path.Movement functions may use L to turn left, R to turn right,
    or a number to move forward that many units.
    '''
    current_direction = (0, -1)
    current_position = (bot_x, bot_y)
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    bot_path = []
    end_path = False

    while not end_path:
        x, y = current_position[0] + current_direction[0], current_position[1] + current_direction[1]

        if map_code[y][x] != 35:
            pass

        end_path = True




def main():
    #Take optcode from file
    opcode_list = fa.read_input_values('day17_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]

    task_map_code = create_map(opcode_list)
    bot_x, bot_y = draw_map(task_map_code)

    result1 = calculate_result_part1(task_map_code)

    ### Print First Result ###
    print('Part1: ', result1)

    calculate_path(opcode_list, bot_x, bot_y)


if __name__ == '__main__':
    main()
