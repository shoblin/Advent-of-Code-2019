#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     17.12.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
template = "Code: {} row={} column={} result={}"

def find_seat(code):
    '''
    Find Row and column of seats:
        Rows 0 through 127
        F means to take the lower half;
        B means to take the upper half;
        8 columns of seats on the plane (numbered 0 through 7)
        R means to take the upper half
        L means to take the lower half
    '''
##    row_min, row_max = 0, 127
##    col_min, col_max = 0, 7
##    row, column = 0, 0

    row =  code[:-3].replace('B', '1')
    row = row.replace('F', '0')
    row = int(row, base= 2)
    col =  code[-3:].replace('R', '1')
    col = col.replace('L', '0')
    col = int(col, base= 2)

    return row, col


def main():
    seats = []

    result = 0
    with open('data/day5_puzzle_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
##            find_seat(line)
            row, col = find_seat (line)
            if result < row * 8 + col:
                result = row * 8 + col
            seats.append(row * 8 + col)
##            print(template.format(line, row, col, row * 8 + col))
    seats.sort()
    print(seats)

##    for rows in seats:
##        print(rows)
    print(f"Solution 2: {[seat for seat in range(min(seats), max(seats)) if seat not in seats]}")

if __name__ == '__main__':
    main()
