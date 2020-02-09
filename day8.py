#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     03.01.2020
# Copyright:   (c) Shoblin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def check_pixel(idy, idx, layers):
    idz = 0
    while layers[idz][idy][idx] == '2':
        idz += 1
    if layers[idz][idy][idx] == '0':
        return '.'
    elif layers[idz][idy][idx] == '1':
        return 'X'

def main():
    img_wide, img_tall = 25, 6
    min_num_zero = img_tall * img_wide

    with open("data//day8_puzzle_input.txt", "r") as file:
        line = file.read()

    lines = [line[i : i + img_wide] for i in range(0,len(line),img_wide)]
    layers = [lines[i : i + img_tall] for i in range(0,len(lines),img_tall)]
    result_lines = [0] * img_wide
    result_layer = [result_lines] * img_tall
    str_result = ""

    for row in range(img_tall):
        for idx in range(img_wide):
            result_layer [row][idx] = check_pixel(row, idx, layers)
        print(result_layer[row])

if __name__ == '__main__':
    main()
