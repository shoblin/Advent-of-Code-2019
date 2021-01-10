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

def read_file(filename):
    data = []
    with open(filename, 'r') as fl:
        for row in fl:
            data.append([st for st in row.strip()])
    return data


def print_map(data):
    '''
    '''
    for row in data:
        print(''.join(row))


def count_occupied_seats(data, pos):
    '''
    '''
    occ_seats = 0
    pos_around = [
        (-1,-1), (-1,0), (-1, 1),
        (0,-1),          (0, 1),
        (1,-1),  (1,0),  (1, 1)]
    for count_pos in [(pos[0]+cur[0], pos[1]+cur[1]) for cur in pos_around]:
        row, col = count_pos
        if row < 0 or col < 0:
            continue
        if row > len(data)-1 or col >len(data[0])-1:
            continue
        if data[row][col] == '#':
            occ_seats +=1

    return occ_seats


def get_seats(data_map):
    '''
    The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    '''
    changes = 0
    copy_map = copy.deepcopy(data_map)
    for row in range(len(data_map)):
        for col in range(len(data_map[0])):
            col_people_around = 0
            if data_map[row][col] != '.':
                col_people_around = count_occupied_seats(data_map, (row, col))
##                print(row, col, col_people_around)
            if data_map[row][col] == 'L' and col_people_around == 0:
                changes +=1
                copy_map[row][col] = '#'
            if data_map[row][col] == '#' and col_people_around >= 4:
                changes +=1
                copy_map[row][col] = 'L'

    data_map = copy.deepcopy(copy_map)
    return changes, data_map


def count_occupied_seats(data, pos):
    '''
    '''
    occ_seats = 0
    pos_around = [
        (-1,-1), (-1,0), (-1, 1),
        (0,-1),          (0, 1),
        (1,-1),  (1,0),  (1, 1)]
    for count_pos in [(pos[0]+cur[0], pos[1]+cur[1]) for cur in pos_around]:
        row, col = count_pos
        if row < 0 or col < 0:
            continue
        if row > len(data)-1 or col >len(data[0])-1:
            continue
        if data[row][col] == '#':
            occ_seats +=1

    return occ_seats


def get_seats2(data_map):
    '''
    The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    '''
    changes = 0
    copy_map = copy.deepcopy(data_map)
    for row in range(len(data_map)):
        for col in range(len(data_map[0])):
            col_people_around = 0
            if data_map[row][col] != '.':
                col_people_around = count_occupied_seats(data_map, (row, col))
##                print(row, col, col_people_around)
            if data_map[row][col] == 'L' and col_people_around == 0:
                changes +=1
                copy_map[row][col] = '#'
            if data_map[row][col] == '#' and col_people_around >= 4:
                changes +=1
                copy_map[row][col] = 'L'

    data_map = copy.deepcopy(copy_map)
    return changes, data_map


def resolve(data_map):
    '''
    '''
    count = 1
    while count >0:
        count, data_map = get_seats(data_map)
    people = 0
    for row in data_map:
        people += row.count('#')
##    print_map(data_map)
    print('Peoples = ', people)


def main():
    data_map = read_file('data/day11_puzzle_input.txt')
    resolve(data_map)


if __name__ == '__main__':
    main()
