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

class Robot_painter:
    '''
    Class of Robot
    Attributes:
    '''
    def __init__ (self, input_vals, init_color = 0):
        self.computer = Computer(input_vals)
        self.direction = 0
        self.x, self.y = 0, 0
        self.painted = {(self.x, self.y): init_color}

    def paint(self):
        while not self.computer.done:
            current_color = self.painted[(self.x, self.y)] if (self.x, self.y) in self.painted else 0
            self.painted[(self.x, self.y)] = self.computer.calculate(current_color)
            self.change_direction(self.computer.calculate())
            self.rotate()

    def change_direction(self, rotate_direction):
        if rotate_direction == 0:
            self.direction = (self.direction - 1) % 4
        else:
            self.direction = (self.direction + 1) % 4

    def rotate(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def show_painting(self):
        data = [["." for _ in range(50)] for _ in range(6)]
        for x, y in self.painted.keys():
            color = self.painted[(x, y)]
            data[abs(y)][x] = "." if color == 0 else "#"
        for row in data:
            print(''.join(row))

def main():
    opcode_list = fa.read_input_values('day11_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]

    painting = Robot_painter(opcode_list)
    painting.paint()
    print(f"Part 1: {len(painting.painted.keys())}")

    letter_painting = Robot_painter(opcode_list[:], 1)
    letter_painting.paint()
    print(f"Part 1: {len(letter_painting.painted.keys())}")
    letter_painting.show_painting()


if __name__ == '__main__':
    main()
