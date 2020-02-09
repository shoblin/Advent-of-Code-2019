#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     16.01.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import itertools
from math import gcd
from functools import reduce

def change_velocity(moon_list):
    for f_moon in moon_list:
        for s_moon in moon_list:
            if f_moon != s_moon:
                f_moon.callculate_velocity(s_moon.coordinates)

def move_moons(moons):
    change_velocity(moons)
    result = 0
    for moon in moons:
        moon.change()
        result += moon.total_energy

    return result

def lcm(a, b):
  return (a * b) // gcd(a, b)

def check_retunting(moons, old_positions):
    idx = 0
    for old_position in old_positions:
        if (moons[idx].coordinates[0] != old_position[0]) or (moons[idx].coordinates[1] != old_position[1]) or moons[idx].coordinates[2] != old_position[2]:
            return True
        idx +=1
    return False


class Moon:
    '''
    Class Moon - moon of Jipiter
    '''
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.velocity = [0, 0, 0]
        self.pot = 0
        self.kin = 0
        self.total_energy = 0

    def callculate_velocity(self, neighbor_coordinates):
        for i in range(3):
            if self.coordinates[i] > neighbor_coordinates[i]:
                self.velocity[i] -= 1
            elif self.coordinates[i] < neighbor_coordinates[i]:
                self.velocity[i] += 1

##        print(self.velocity)

    def change(self):
        for i in range(3):
            self.coordinates[i] += self.velocity[i]
        self.pot = sum([abs(x) for x in self.coordinates])
        self.kin = sum([abs(x) for x in self.velocity])
        self.total_energy = self.pot * self.kin

def main():
    part = input('What part:')
    coordinates =[[-1, 7, 3],
                [12, 2, -13],
                [14, 18, -8],
                [17, 4, -4]]

    moons = []
    for coordinate in coordinates:
            moons.append(Moon(coordinate))

    if part == '1':
        for i in range(1000):
            result = move_moons(moons)

        print ('Part 1', result)

    elif part == '2':
        step = 0
        period =  dict()
        '''
          We will capture the orbital periods (https://en.wikipedia.org/wiki/Orbital_period) for each axis here:
          {
            0: step at which all 4 moons are at their starting x-position and x-velocity
            1: step at which all 4 moons are at their starting y-position and y-velocity
            2: step at which all 4 moons are at their starting z-position and z-velocity
          }
        '''
        start = [[(moon.coordinates[axis], moon.velocity[axis]) for moon in moons] for axis in range(3)]

        while len(period) < 3:
            step += 1
            move_moons(moons)

            for axis in range(3):

                if axis not in period and start[axis] == [(moon.coordinates[axis], moon.velocity[axis]) for moon in moons]:
                    period[axis] = step


        result = reduce(lcm, period.values())
        print('Количеств цыклов, что бы спутники пернулись в изначальное положение: ', result)

if __name__ == '__main__':
    main()
