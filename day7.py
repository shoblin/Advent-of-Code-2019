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
from lib.intcode import Computer
import lib.functions_au as fa

def next_step(lst):
    '''
    Next step of transposition
    '''

    j = len(lst) - 2
    k = len(lst) - 1
    while (lst[j] >= lst[j + 1]):
        j -= 1
    if j < 0:
        return False
    while (lst[j] >= lst[k]):
        k -= 1
    lst[j], lst[k] = lst [k], lst[j]
    l, r = j + 1, len(lst) - 1
    while l < r:
        lst[l], lst[r] = lst [r], lst[l]
        l += 1
        r -= 1
    return True

def main():
    opcode_list = fa.read_input_values('day7_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]

    ls = [x for x in range(5)]
    ls_full = [ls[:]]
    while next_step(ls):
        ls_full.append(ls[:])

    max_output_signal = 0
    for ls_permutation in ls_full:
        output_signal = 0
        for phase in ls_permutation:
            amp = Computer(opcode_list[:])
            amp.inputs.append(phase)
            output_signal = amp.calculate(output_signal)

        max_output_signal = max(max_output_signal, output_signal)

    print('Part1:', max_output_signal)

    ls = [x for x in range(5,10)]
    ls_full = [ls[:]]
    while next_step(ls):
        ls_full.append(ls[:])

    max_output_signal = 0
    for ls_permutation in ls_full:
        output_signal = 0
        amps = [Computer(opcode_list) for _ in range(5)]
        for amp, phase_setting in zip(amps, ls_permutation):
            amp.inputs.append(phase_setting)

        while amps[-1].done == False:
            for amp in amps:
                amp.calculate(output_signal)
                output_signal = amp.output

        max_output_signal = max(output_signal, max_output_signal)
    print(f"Part 2: {max_output_signal}")




if __name__ == '__main__':
    main()
