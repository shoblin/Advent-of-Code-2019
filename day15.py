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

template = """
Position:{},
Cache: {},
Seen_Cells:{}"""


class Repair_Droid:
    '''
    Class of Repair Droid
    Attributes:
        pos - position of repair droid, start position (0, 0)

    Input insruction = four movement commands:
    Move cross:
        north(1), south(2), west(3), east(4)
        1
      3   4
        2

    OUTPUT
    The repair droid can reply with any of the following status codes:
        0: The repair droid hit a wall. Its position has not changed.
        1: The repair droid has moved one step in the requested direction.
        2: The repair droid has moved one step in the requested direction;
           its new position is the location of the oxygen system.
    '''
    DIR = {1: (0, 1),
           2: (0,-1),
           3: (-1,0),
           4: (1, 0)}

    REV = {1: 2,
           2: 1,
           3: 4,
           4: 3}

    def __init__(self, comp):
        self.pos = (0, 0)
        self.comp = comp
        self.cell_seen = set([self.pos])
        self.cache =[]



    def step(self, direction):
        return (self.pos[0] + self.DIR[direction][0], self.pos[1] + self.DIR[direction][1])

    def move_back(self):
        print("*" *5, self.pos)
        last_move = self.cache.pop()
        revmove = self.REV[last_move]
        self.pos = self.step(revmove)
        self.comp.calculate(revmove)

##    def check

    def run(self):
        while True:
##        for _ in range(50):
            for dir in range(1, 6):

                #Dead
                if dir == 5:
                    self.move_back()
                    break

                cell_position = self.step(dir)

                if cell_position in self.cell_seen:
                    continue

                self.cell_seen.add(cell_position)

                droid_code = self.comp.calculate(dir)

                if droid_code == 0:
                    continue
                if droid_code == 1:
                    self.pos = self.step(dir)
                    self.cache.append(dir)
                    break
                if droid_code == 2:
                    print("Yahooo")
                    return
##            print(template.format(cell_position, self.cache, self.cell_seen))





##    def look_around(self):
##        num_walls = 0
##        for dir in range(4):
##            status_code = self.comp.calculate(dir)
##            cell_position = step(dir)
##            if status_code == 0:
##                num_walls += 1
##                self._map[cell_position] = 0
##            if status_code == 1:
##                print(cell_position, ".")
##                self.comp.calculate(self.REV[dir])
##            if status_code == 2:
##                print("YAHOO")


def main():

    opcode_list = fa.read_input_values('day15_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]

    computer = Computer(opcode_list)
    droid = Repair_Droid(computer)
    droid.run()
    print(len(droid.cache))


if __name__ == '__main__':
    main()
