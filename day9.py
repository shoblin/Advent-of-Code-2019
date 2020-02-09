#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     02.01.2020
# Copyright:   (c) Shoblin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import lib.functions_au as fa
from lib.intcode import Computer

def main():
    opcode_list = fa.read_input_values('day9_puzzle_input.txt')
    opcode_list = opcode_list + [0] * 2000
    opcode_list = [int(thing) for thing in opcode_list]

    input_signal = 1
    amp1 = Computer(opcode_list[:])
    output_signal1 = amp1.calculate(input_signal)
    print(output_signal1)

    input_signal = 2
    amp2 = Computer(opcode_list[:])
    output_signal2 = amp2.calculate(input_signal)
    print (output_signal2)


if __name__ == '__main__':
    main()
