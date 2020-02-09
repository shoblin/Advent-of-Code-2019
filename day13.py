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

def main():
    opcode_list = fa.read_input_values('data\\day13_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]
    computer = Computer(opcode_list)

    blocks_num = 0

    game_ch = {
        0: ' ',
        1: '|',
        2: '#',
        3: '-',
        4: '0'}

    game_code = []
    while not computer.done:
        output = computer.calculate()
        if not computer.done:
            game_code.append(output)

    game_map = [['.' for _ in range(43)] for _ in range(23)]
    for idx in range(0,len(game_code),3):
        if game_code[idx+2] == 2 : blocks_num +=1
        x, y, ch = game_code[idx], game_code[idx+1], game_ch[game_code[idx+2]]

##        print(idx, x,y,ch)
        game_map[y][x] = ch
    result = 0
    for row in game_map:
        print(row)
        result += row.count('#')

    print(result, blocks_num)

if __name__ == '__main__':
    main()
