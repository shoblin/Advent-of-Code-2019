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
import lib.functions_au as fa

def new_coordinate(code, last_x, last_y):
    '''
    Function for transform instruction into coordinates
	R - add value to coordinate of X
	L - substract valur from coordinate of X
	U - add value to coordinate ofY
	D - substract valur from coordinate ofY
    '''

    if code[0] == 'R':
        new_x = last_x + int(code[1:])
        new_y = last_y
    elif code[0] == 'L':
        new_x = last_x - int(code[1:])
        new_y = last_y
    elif code[0] == 'U':
        new_x = last_x
        new_y = last_y + int(code[1:])
    elif code[0] == 'D':
        new_x = last_x
        new_y = last_y - int(code[1:])

    return new_x, new_y

def build_wire(list):
    '''
    Function to create two lists with coordinates of points
    '''
    wire_x_cord = [0]
    wire_y_cord = [0]

    for code in list:
        new_coordinate(code, wire_x_cord[-1], wire_y_cord[-1])
        nx, ny = new_coordinate(code, wire_x_cord[-1], wire_y_cord[-1])
        wire_x_cord.append(nx)
        wire_y_cord.append(ny)

    return (wire_x_cord, wire_y_cord)



def main():
    list1 = fa.read_input_values('data\\day3_puzzle_input.txt')
    list2 = fa.read_input_values('data\\day3_puzzle_input.txt', 1)

    wire1 = []
    wire2 = []
    wire1.append(build_wire(list1))
    print(wire1)
    wire2.append(build_wire(list2))

    print(wire2)




if __name__ == '__main__':
    main()
