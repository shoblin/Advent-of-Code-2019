#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     26.12.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def open_file_bags(filename):

    with open(filename, 'r') as file:
        for line in file:
            line = line.split()
            bag, recipe = line.strip('contain')




def main():
    bags = open_file_bags('data/puzzle_input.txt')


if __name__ == '__main__':
    main()
