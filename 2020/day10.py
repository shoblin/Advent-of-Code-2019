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

def read_file(filename):
    data = []
    with open(filename, 'r') as fl:
        for line in fl:
            data.append(int(line))

    return data

def main():
    curr_jolt = 0
    jolts_1, jolts_3 = 0, 1
    data = read_file('data/day10_puzzle_input.txt')
    data.sort()
##    print(data)
    for nxt_jolt in data:
        delta = nxt_jolt - curr_jolt
##        print(curr_jolt, nxt_jolt, delta)
        if delta == 1:
            jolts_1 += 1
        elif delta == 3:
            jolts_3 += 1

        curr_jolt = nxt_jolt

    print ('Solution part1:',jolts_1 * jolts_3)

    sol = {0:1}
    for line in data:
        sol[line] = 0
        if line - 1 in sol:
            sol[line] += sol[line - 1]
        if line - 2 in sol:
            sol[line] += sol[line - 2]
        if line - 3 in sol:
            sol[line] += sol[line - 3]

    print(sol[max(data)])

if __name__ == '__main__':
    main()
