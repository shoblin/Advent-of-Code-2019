#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     12.12.2019
# Copyright:   (c) Shoblin 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lib.intcode import Computer
import lib.functions_au as fa

def check_instruction(current_opcode):
    '''
              ABCDE
    Example:   1002

    DE - two-digit opcode,      02 == opcode 2
    C - mode of 1st parameter,  0 == position mode
    B - mode of 2nd parameter,  1 == immediate mode
    A - mode of 3rd parameter,  0 == position mode,
    '''
    #divided opcode into 4 sections
    instruction_full = [0, 0, 0, 0]
    current_opcode = str(current_opcode)
    instruction_full[-1] = int(current_opcode[-2:])

    if  len(current_opcode) >= 3:
        instruction_full[-2] = int(current_opcode[-3])
    if  len(current_opcode) >= 4:
        instruction_full[-3] = int(current_opcode[-4])
    if  len(current_opcode) == 5:
        instruction_full[-4] = int(current_opcode[-5])

    return instruction_full

def main():
    current_position = 0
    opcode_list = fa.read_input_values('data\\day5_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]

    computer = Computer(opcode_list)

    while not computer.done:
        computer.calculate(5)
    print(computer.output)

if __name__ == '__main__':
    main()
