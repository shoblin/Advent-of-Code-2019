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
import functions_au as fa

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


class Amp:
    '''
    Class of Amplifiers
    Attributes:

    '''
    def __init__ (self, data):
        self.position = 0
        self.data = data[:]
        self.done = False
        self.output = None
        self.base = 0
        self.inputs = []

    def get_params(self, mode1, mode2, mode3):
        '''Take two modes of two parametrs and return values of parametrs'''
        return self.get_param(mode1, 1), self.get_param(mode2, 2),  self.get_param(mode3, 3)

    def get_param(self, mode, increment):
        '''
        0 == position mode
        1 == immediate mode
        2 == relative mode
        '''

        if mode == 0:
            return self.data[self.position + increment]
        elif mode == 1:
            return self.position + increment
        elif mode == 2:
            return self.data[self.position + increment] + self.base

    def check_instruction(self, current_opcode):
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

    def calculate(self, input_val):
        self.inputs.append(input_val)
        while True:
            current_instruction = self.check_instruction(self.data[self.position])

            digit_opcode = current_instruction[-1]
            f_mode, s_mode, t_mode  = current_instruction[-2], current_instruction[-3], current_instruction[-4]

            f_param, s_param, t_param = self.get_params(f_mode, s_mode, t_mode)

            if digit_opcode == 1:
                self.data[t_param] = self.data[f_param] + self.data[s_param]
                self.position += 4

            elif digit_opcode == 2:
                self.data[t_param] = self.data[f_param] * self.data[s_param]
                self.position += 4

            elif digit_opcode == 3:
                self.data[f_param] = self.inputs.pop(0)
                self.position += 2

            elif digit_opcode == 4:
                self.output = self.data[f_param]
                self.position += 2
                return self.output

            elif digit_opcode == 5:
                if self.data[f_param] != 0:
                    self.position = self.data[s_param]
                else:
                    self.position += 3

            elif digit_opcode == 6:
                if self.data[f_param] == 0:
                    self.position = self.data[s_param]
                else:
                    self.position += 3

            elif digit_opcode == 7:
                if self.data[f_param] < self.data[s_param]:
                    self.data[t_param] = 1
                else:
                    self.data[t_param] = 0
                self.position += 4

            elif digit_opcode == 8:
                if self.data[f_param] == self.data[s_param]:
                    self.data[t_param] = 1
                else:
                    self.data[t_param] = 0
                self.position += 4

            elif digit_opcode == 9:
                self.base += self.data[f_param]
                self.position += 2

            elif digit_opcode == 99:
                self.done = True
##                print(self.data)
                return self.output

def main():
    opcode_list = fa.read_input_values('day9_puzzle_input.txt')
    opcode_list = opcode_list + [0] * 2000
    opcode_list = [int(thing) for thing in opcode_list]

##    opcode_list =[1102,34915192,34915192,7,4,7,99,0] + [0] * 1000
    input_signal = 2
    amp = Amp(opcode_list[:])
    output_signal = amp.calculate(input_signal)
    print (output_signal)




##    ls = [x for x in range(5)]
##    ls_full = [ls[:]]
##    while next_step(ls):
##        ls_full.append(ls[:])
##
##    max_output_signal = 0
##    for ls_permutation in ls_full:
##        output_signal = 0
##        for phase in ls_permutation:
##            amp = Amp(opcode_list[:])
##            amp.inputs.append(phase)
##            output_signal = amp.calculate(output_signal)
##
##        max_output_signal = max(max_output_signal, output_signal)
##
##    print('Part1:', max_output_signal)
##
##    ls = [x for x in range(5,10)]
##    ls_full = [ls[:]]
##    while next_step(ls):
##        ls_full.append(ls[:])
##
##    max_output_signal = 0
##    for ls_permutation in ls_full:
##        output_signal = 0
##        amps = [Amp(opcode_list) for _ in range(5)]
##        for amp, phase_setting in zip(amps, ls_permutation):
##            amp.inputs.append(phase_setting)
##
##        while amps[-1].done == False:
##            for amp in amps:
##                output_signal = amp.calculate(output_signal)
####            print(output_signal)
##        max_output_signal = max(output_signal, max_output_signal)
##    print(f"Part 2: {max_output_signal}")




if __name__ == '__main__':
    main()
