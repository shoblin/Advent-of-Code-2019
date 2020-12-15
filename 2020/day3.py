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

def sliding(map_list, step):
    '''
    Count trees on path(1,3)
    '''
    current_position = [0, 0]

    trees = 0

    for row in map_list:
        len_row = len(row)
        current_position [0]= current_position[0] + step[0]
        current_position [1]= current_position[1] + step[1]

        if current_position[1] >= len_row:
            current_position[1] -= len_row
##            print(current_position[0], current_position[1])
        y, x = current_position

        if y < len(map_list):
            if map_list[y][x] == '#':
                trees += 1
    return trees



def main():
    map_list = fa.read_maps('data/day3_puzzle_input.txt')
##    print(sliding(map_list,(1,3)))

    result_task2 = 1
    steps = [(1,1),(1,3),(1,5),(1,7),(2,1)]

    for step in steps:
        print(sliding(map_list,step))
        result_task2 *= sliding(map_list,step)

    print ('result =',result_task2)

##    for map_row in map_list:
##        print(map_row)

if __name__ == '__main__':
    main()
