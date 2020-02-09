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

def main():
    img_wide, img_tall = 25, 6
    min_num_zero = img_tall * img_wide
    required_layer = 0
    idx = -1

    with open("day8_puzzle_input.txt", "r") as file:
        line = file.read()

    divided_text = [line[i : i + img_wide * img_tall] for i in range(0,len(line),img_wide * img_tall)]

    for part_text in divided_text:

        idx += 1
        if min_num_zero >  part_text.count('0'):
            required_layer = idx
            min_num_zero = part_text.count('0')

    required_layer_img = divided_text[required_layer]
    result = required_layer_img.count('1')  *  required_layer_img.count('2')

    print(result)



if __name__ == '__main__':
    main()
