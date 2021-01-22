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
import math

def read_file(filename):
    data = []
    with open(filename, 'r') as fl:
        for row in fl:
            row = row.strip()
            data.append([row[0], int(row[1:])])
    return data

##def forward(pos, face, value):
##        dirs = [(0, 1),(1,0),(0, -1),(-1,0)]
##        return (pos[0] + value * dirs[face][0], pos[1] + value * dirs[face][1])

def turn(way_point, angle):
        r_angle = math.radians(angle)
        x, y = way_point
        x1 = round(x*math.cos(r_angle) - y*math.sin(r_angle))
        y1 = round(x*math.sin(r_angle) + y*math.cos(r_angle))
        return (x1, y1)


def run_ship(data):
    '''
    first position = (0, 0)
    '''
    ## diewction E=(0,1) S=(1, 0) W=(0, -1) N=(-1, 0)
    dirs = {'E':(1, 0),'S':(0, 1),'W':(-1, 0),'N':(0, -1)}

    pos = (0, 0) # current position
    way_point = (10, -1)

    for cm, val in data:

        if cm == 'L':
            way_point = turn(way_point, -val)
        if cm == 'R':
            way_point = turn(way_point, val)
        #################################
        ##        Move waypoint        ##
        #################################
        if dirs.get(cm):
            x, y = way_point
            x += dirs[cm][0] * val
            y += dirs[cm][1] * val
            way_point = (x, y)
##        if d[0] == 'N':
##            pos = forward(pos, 3, d[1])
##        if d[0] == 'E':
##            pos = forward(pos, 0, d[1])
##        if d[0] == 'S':
##            pos = forward(pos, 1, d[1])
##        if d[0] == 'W':
##            pos = forward(pos, 2, d[1])
        #################################
        if cm == 'F':
            pos= (pos[0] + way_point[0] * val, pos[1] + way_point[1] * val )

##        print(way_point, pos)
##
    print(abs(pos[0])+abs(pos[1]))


def main():
    data_map = read_file('data/day12_puzzle_input.txt')
    run_ship(data_map)






if __name__ == '__main__':
    main()
