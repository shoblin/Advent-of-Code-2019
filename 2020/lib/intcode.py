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

class Computer:
    '''
    Class of Amplifiers
    Attributes:
        position - position of execute code
        memory - list of intcode
        done - marker of ending code. Command for ending: 99
        output -
        base - posirion for relative mode
        input - list with inputs
    '''
    def __init__ (self, data):
        self.position = 0
        self.memory = data[:] + [0] * 3000
        self.done = False
        self.output = None
        self.base = 0
        self.inputs = []

    def get_params(self, mode1, mode2, mode3):
        '''Take two modes of two parametrs and return values of parametrs'''
        return self.get_param(mode1, 1), self.get_param(mode2, 2),  self.get_param(mode3, 3)

    def get_param(self, mode, increment):
        '''
        Return part of
        0 == position mode
        1 == immediate mode
        2 == relative mode
        '''

        if mode == 0:
            return self.memory[self.position + increment]
        elif mode == 1:
            return self.position + increment
        elif mode == 2:
            return self.memory[self.position + increment] + self.base

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

    def calculate(self, input_val = None):
        if input_val is not None: self.inputs.append(input_val)
        while True:
            current_instruction = self.check_instruction(self.memory[self.position])

            digit_opcode = current_instruction[-1]
            f_mode, s_mode, t_mode  = current_instruction[-2], current_instruction[-3], current_instruction[-4]

            f_param, s_param, t_param = self.get_params(f_mode, s_mode, t_mode)

            # 1: sum
            if digit_opcode == 1:
                self.memory[t_param] = self.memory[f_param] + self.memory[s_param]
                self.position += 4

            # 2: multiply
            elif digit_opcode == 2:
                self.memory[t_param] = self.memory[f_param] * self.memory[s_param]
                self.position += 4

            #3: input
            elif digit_opcode == 3:
                self.memory[f_param] = self.inputs.pop(0)
                self.position += 2

            #4: otput
            elif digit_opcode == 4:
                self.output = self.memory[f_param]
                self.position += 2
                return self.output

            # 5: jump-if-true
            elif digit_opcode == 5:
                if self.memory[f_param] != 0:
                    self.position = self.memory[s_param]
                else:
                    self.position += 3

            #6: jump-if-false
            elif digit_opcode == 6:
                if self.memory[f_param] == 0:
                    self.position = self.memory[s_param]
                else:
                    self.position += 3

            # 7: less than
            elif digit_opcode == 7:
                if self.memory[f_param] < self.memory[s_param]:
                    self.memory[t_param] = 1
                else:
                    self.memory[t_param] = 0
                self.position += 4

            # 8: equal
            elif digit_opcode == 8:
                if self.memory[f_param] == self.memory[s_param]:
                    self.memory[t_param] = 1
                else:
                    self.memory[t_param] = 0
                self.position += 4

            # 9: set relative base
            elif digit_opcode == 9:
                self.base += self.memory[f_param]
                self.position += 2

            # 99: end
            elif digit_opcode == 99:
                self.done = True
##                print('END')
                break

            else:
                raise ValueError(f'ERRRRR... p: {self.position}, op: {digit_opcode}, v: {self.memory[self.position]}')