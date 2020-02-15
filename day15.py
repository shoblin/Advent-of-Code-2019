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

    #Direction for moving
    DIR = {1: (0, 1),
           2: (0,-1),
           3: (-1,0),
           4: (1, 0)}

    #Direction for returning
    REV = {1: 2,
           2: 1,
           3: 4,
           4: 3}

    def __init__(self, comp):
        self.pos = (0, 0) # Current position of droid
        self.comp = comp  # Create copy of Computer for calculate optcode
        self.cell_seen = set([self.pos]) # Set with all cell what we check
        self.cache =[]    # List with commands for droids

        self.map = {self.pos: True}
        self.oxygen = None

    def step(self, direction):
        return (self.pos[0] + self.DIR[direction][0], self.pos[1] + self.DIR[direction][1])

    def move_back(self):
##        print(self.pos)
        last_move = self.cache.pop()
        revmove = self.REV[last_move]
        self.pos = self.step(revmove)
        self.comp.calculate(revmove)

##    def check

    def run(self):
        while True:
            for dir in [4, 3, 2, 1, 5]:

                #Dead end -
                if dir == 5:
                    self.move_back()
                    break

                cell_position = self.step(dir)

                if cell_position in self.cell_seen:
                    continue

                self.cell_seen.add(cell_position)

                droid_code = self.comp.calculate(dir)

                if droid_code == 0:
                    self.map[cell_position] = False
                    continue
                if droid_code == 1:
                    self.pos = self.step(dir)
                    self.cache.append(dir)
                    self.map[cell_position] = True
                    break
                if droid_code == 2:
                    self.oxygen = cell_position
                    self.cache.extend([dir, 0])
                    self.map[cell_position] = True
                    return

def main():
    #Take optcode from file
    opcode_list = fa.read_input_values('day15_puzzle_input.txt')
    opcode_list = [int(thing) for thing in opcode_list]

    #First part of task. Find path to oxigen system
    computer = Computer(opcode_list)
    droid = Repair_Droid(computer)
    droid.run()
    print("Part 1:",len(droid.cache))

    map_min_x, map_max_x, map_min_y, map_max_y = 0, 0, 0, 0
    for key in droid.map:
        map_max_x = max(map_max_x, key[0])
        map_min_x = min(map_min_x, key[0])
        map_max_y = max(map_max_y, key[1])
        map_min_y = min(map_min_x, key[1])

    visible_map = [[ " " for _ in range(map_max_x - map_min_x + 1)] for _ in range(map_max_y - map_min_y + 1)]

    ox_x, ox_y = droid.oxygen

    for key in droid.map:
        x = key[0] - map_min_x
        y = key[1] - map_min_y
        if droid.map[key]:
            visible_map[y][x] = " "
        else:
            visible_map[y][x] = "#"
    visible_map[-map_min_y][-map_min_x] = "0"
    visible_map[ox_y-map_min_y][ox_x-map_min_x] = "W"

    print("*" * 70, " MAP ", "*" * 70 )
    for row in visible_map:
        print(row)


    oxigen_front = [(droid.oxygen, 0)]
    system_map = droid.map
    ox = set()

    while oxigen_front:
##    for _ in range(20):
        cell = oxigen_front.pop(0)

        if cell[0] in ox:
            continue
        step = cell[1]
        ox.add(cell[0])

        for dir in [(1,0), (0,1), (-1,0), (0,-1)]:
            new_position = (cell[0][0] + dir[0],cell[0][1] + dir[1])
            if new_position not in system_map or new_position in ox:
                continue
            if system_map[new_position]:
                oxigen_front.append((new_position, cell[1] + 1))

    print("*" * 140)

    print("Part 2:", step)





if __name__ == '__main__':
    main()
