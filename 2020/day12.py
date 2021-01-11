#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     07.01.2021
# Copyright:   (c) atopolskiy 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import copy

##class Boat:
##    ''' '''
##    def __init__(self):
##        self.dirs = [(0, 1),(1,0),(0, -1),(-1,0)]
##        self.face = 0
##        self.pos = (0, 0)
##
##
##    def turn_left(self, angle):
##        x = angle // 90
##        self.face = (self.face - x) % 4
##
##
##    def turn_right(self, angle):
##        x = angle // 90
##        self.face = (self.face + x) % 4
##
##
##    def forward(self, value):
##        dir = self.dirs[self.face]
##        self.pos = (self.pos[0] + value * dir[0], self.pos[1] + value * dir[1])
##
##
##    def go_side(self, face):
##        dir = self.dirs[face]
##        self.pos = (self.pos[0] + value * dir[0], self.pos[1] + value * dir[1])


def read_file(filename):
    data = []
    with open(filename, 'r') as fl:
        for row in fl:
            row = row.strip()
            data.append([row[0], int(row[1:])])
    return data

def forward(pos, face, value):
        dirs = [(0, 1),(1,0),(0, -1),(-1,0)]
        return (pos[0] + value * dirs[face][0], pos[1] + value * dirs[face][1])

def turn_left(face, angle):
        return (face - angle // 90) % 4

def turn_right(face, angle):
        return (face + angle // 90) % 4

def run_ship(data):
    '''
    first position = (0, 0)
    '''
    ## diewction E=(0,1) S=(1, 0) W=(0, -1) N=(-1, 0)
    dirs = [(0, 1),(1,0),(0, -1),(-1,0)]
    face = 0 # current direction the ship is facing
    pos = (0, 0) # current position

    for d in data:

        if d[0] == 'L':
            face = turn_left(face, d[1])
        if d[0] == 'R':
            face = turn_right(face, d[1])
        #################################
        if d[0] == 'N':
            pos = forward(pos, 3, d[1])
        if d[0] == 'E':
            pos = forward(pos, 0, d[1])
        if d[0] == 'S':
            pos = forward(pos, 1, d[1])
        if d[0] == 'W':
            pos = forward(pos, 2, d[1])
        #################################
        if d[0] == 'F':
            pos = forward(pos, face, d[1])

    print(abs(pos[0])+abs(pos[1]))


def main():
    data_map = read_file('data/day12_puzzle_input.txt')
    run_ship(data_map)





if __name__ == '__main__':
    main()
