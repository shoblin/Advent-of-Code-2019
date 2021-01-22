#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     13.01.2021
# Copyright:   (c) Shoblin 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def read_file(filename):
    with open(filename, 'r') as fl:
        time = fl.readline().strip()
        sch = fl.readline().split(',')

    return int(time), sch

def main():
    time, delays = read_file ('data/day13_puzzle_input.txt')

    min_time = None
    min_id = 0

    for  d in delays:
        if d != 'x':
            d = int(d)
            full_counts =   time // d
            remainder = time % d
            if remainder == 0:
                print("In the time", d)
            else:
                full_counts += 1
                remainder =  full_counts * d - time
                if min_id == 0:
                    min_id = d
                    min_time = remainder
                if min_time > remainder:
                    min_id = d
                    min_time = remainder


    print(min_id, min_time,min_id*min_time)


if __name__ == '__main__':
    main()
