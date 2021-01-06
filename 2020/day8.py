#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     26.12.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def open_file(file_name):
    '''
    Get lines from file and create list with them
    '''
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line.strip('.\n'))

    return lines


def split_command(data):
    '''
    Work with information from file
    '''
    lines = []
    for line in data:
        cmd, chng = line.split()

        lines.append([cmd, chng])

    return lines


def change_value(old_value, instruction):
    '''
    Value add or subtract in a old value
    '''
    return old_value + int(instruction)


def solution(lines):
    '''
    Run program and try find infinite loop
    As result we print what value is in the accumulator
    '''
    acc = 0
    move = 0
    executed_moves = []
    ended =False

    while move not in executed_moves and not ended:
        num_move +=1
        executed_moves.append(move)

        instruction = lines[move]
        if instruction[0] == 'nop':
            move += 1
        elif instruction[0] == 'acc':
            move += 1
            acc = change_value(acc, instruction[1])
        elif instruction[0] == 'jmp':
            move = change_value(move, instruction[1])

        ended = move == len(lines)

    return ended, acc


def solution2(lines):



def main():
    data = open_file('data/day8_puzzle_input.txt')
    lines = split_command(data)
    print(solution(lines))

    print('*'*15)
    print(solution2(lines))


if __name__ == '__main__':
    main()
