#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     17.01.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lib.intcode import Computer
import lib.functions_au as fa

def draw_screen(game_map):
    for row in game_map:
        print(row)

def joystick_position(ball_pos, paddle_pos, comp):

    if ball_pos > paddle_pos:
        comp.inputs.append(1)
    elif ball_pos < paddle_pos:
        comp.inputs.append(-1)
    elif ball_pos == paddle_pos:
        comp.inputs.append(0)

def main():
    opcode_list = fa.read_input_values('day13_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]
    opcode_list[0] = 2
    computer = Computer(opcode_list)


    ball_x = 0
    paddle_x = 0
    joystick_input = 0
    scrole = 0

    game_ch = {
        0: ' ',
        1: '|',
        2: '#',
        3: '-',
        4: '0'}
    game_code = {}

    blocks_num = 0
    ball_draw = False
    paddle_draw = False

    while not computer.done:
        x = computer.calculate()
        y = computer.calculate()
        title = computer.calculate()
        if not (x == -1 and y == 0):
            if title != None:
                game_code[(x, y)] = game_ch[title]
        elif x == -1 and y == 0 :
            scrole = title

        if title == 3:
            paddle_x = x
            paddle_draw = True
            if ball_draw == True:
                ball_draw = False
                paddle_draw = False
                joystick_position(ball_x, paddle_x, computer)

        elif title == 4:
            ball_x = x
            ball_draw = True
            if paddle_draw == True or paddle_x !=0:
                ball_draw = False
                paddle_draw = False
                joystick_position(ball_x, paddle_x, computer)



        elif title == 2:
            blocks_num += 1
##        if blocks_num == 0:
##            break

##        computer.done = False

    print('*' * 20)
    print('* Scrole:', f'{scrole:8}','*')
    print('*' * 20)

if __name__ == '__main__':
    main()
