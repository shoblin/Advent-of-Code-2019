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
import operator

def build_wire(list, wire):
    '''
    Function to create two lists with coordinates of points
    '''
    x, y = 0, 0
    steps = 0

    for code in list:
        lenght = int(code[1:])

        for _ in range(lenght):
            if code[0] == 'R':
                x += 1
            elif code[0] == 'L':
                x -= 1
            elif code[0] == 'U':
                y += 1
            elif code[0] == 'D':
                y -= 1
            steps += 1
            wire[(x,y)] = steps

    return wire

def manhattan_distance(coord):
    return abs(coord[0]) + abs(coord[1])


def main():
    template = "Part{} Answer: {}"

    list1 = fa.read_input_values('day3_puzzle_input.txt')
    list2 = fa.read_input_values('day3_puzzle_input.txt', 1)

    wire1 = build_wire(list1, {})
    wire2 = build_wire(list2, {})

    cross_wire = list(set(wire1.keys()) & set(wire2.keys()))

    result1 = manhattan_distance(cross_wire[0])
    for coord in cross_wire:
        result1 = min(result1, manhattan_distance(coord))

    print(template.format(1, result1))


    steps = wire1[cross_wire[0]] + wire2[cross_wire[0]]
    for coord in cross_wire:
        if steps > wire1[coord] + wire2[coord]:
            steps = wire1[coord] + wire2[coord]

    print(template.format(2, steps))


if __name__ == '__main__':
    main()
