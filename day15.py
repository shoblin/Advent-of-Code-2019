#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     09.02.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lib.intcode import Computer
import lib.functions_au as fa

def main():
    opcode_list = fa.read_input_values('day15_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]

    computer = Computer(opcode_list)
    computer.calculate(1)
    d = computer.memory[:]
    print(computer.output)
    computer.calculate(1)
    print(computer.output, d == computer.memory)
    computer.calculate(1)
    print(computer.output)

    print(computer.output)

if __name__ == '__main__':
    main()
