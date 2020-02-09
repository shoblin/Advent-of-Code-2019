#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     10.01.2020
# Copyright:   (c) Shoblin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import functions_au as au
import math
import operator

def take_ast_coordinates(task_map):
    '''
    Transform "map" list into coordination
    '''
    result = []
    idy = 0
    for row in task_map:
        for idx in range(len(row)):
            if row[idx] == '#':
                cord = (idx, idy)
                result.append(cord[:])
        idy +=1

    return result

def angle(start, end):
    ''' '''
    dx = end[0] - start[0]
    dy = start[1] - end[1]
    angle_result = math.atan2(dx, dy) * 180/math.pi
    if angle_result < 0:
        return 360 + angle_result

    return angle_result


def count_visible_ast(ast_cord, ast_map):
    '''
    find visible asteroids
    '''
    visible_angel = []
    for other_ast in ast_map:
        angle_current = angle(ast_cord, other_ast)
        if (angle_current not in visible_angel):
            visible_angel.append(angle_current)

    return len(visible_angel)

def find_best_ast(asteroids):
    '''
    Find coodinations of asteroid for a new monitoring station
    '''
    max_val = 0
    cord_mon_station = None
    for asteroid_cord, asteroid_val in asteroids.items():
        if asteroid_val > max_val:
            max_val = asteroid_val
            cord_mon_station = asteroid_cord

    return cord_mon_station

def count_distance(start, end):

    return ((start[0] - end[0]) **2 +(start[1] - end[1])**2)

def sort_distance(start, asteroids_on_one_line):
    '''Function for sort asteroids by distance'''
    result = {asteroid: count_distance(start, asteroid) for asteroid in asteroids_on_one_line}

    result = sorted(result, key=operator.itemgetter(1))
    return result



def create_dict_asteroids(monitor_station, map_list):
    '''
    Create dictionary {angle, sorted[coordinates]}
    '''
    sort_dict = {}
    angles = []
    for asteroid in map_list:
        curr_angel = angle(monitor_station, asteroid)
        if curr_angel in angles:
            sort_dict[curr_angel].append(asteroid)
        else:
            angles.append(curr_angel)
            sort_dict[curr_angel] = [asteroid]
    angles = sorted(angles)
    for curr_angel in angles:
        sort_dict[curr_angel] = sort_distance(monitor_station,sort_dict[curr_angel])
    return angles, sort_dict

def main():
    task_list = au.reed_maps('data//day10_puzzle_input.txt')
    asts_cord = take_ast_coordinates(task_list)

    result_dict = {}
    for ast_cord in asts_cord:
        result_dict[ast_cord] = count_visible_ast(ast_cord,asts_cord)

    best_cord = find_best_ast(result_dict)
    print ('Part1: ', max(result_dict.values()))

    asts_cord.remove(best_cord)

    angels, dict_asteroids = create_dict_asteroids(best_cord, asts_cord)

    idx, cnt = 0, 0
    while cnt <200:
        result_cord = dict_asteroids[angels[idx]]
        result_cord = result_cord.pop(0)
        cnt += 1
        if len(dict_asteroids[angels[idx]]) <= 0:

            angels.pop(idx)
            continue

        idx += 1
        if idx > len(angels):
            idx = 0

    print('Part1: ', result_cord[0] * 100 + result_cord[1])

if __name__ == '__main__':
    main()
