#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     30.12.2019
# Copyright:   (c) atopolskiy 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def next_step(lst):
    '''
    Next step of transposition
    '''

    j = len(lst) - 2
    k = len(lst) - 1
    while (lst[j] >= lst[j + 1]):
        j -= 1
    if j < 0:
        return False
    while (lst[j] >= lst[k]):
        k -= 1
    lst[j], lst[k] = lst [k], lst[j]
    l, r = j + 1, len(lst) - 1
    while l < r:
        lst[l], lst[r] = lst [r], lst[l]
        l += 1
        r -= 1
    return True



def main():
    ls = [x for x in range(1,5)]
    ls_full = []
    while next_step(ls):
        ls_full.append(ls[:])

    print(ls_full)


if __name__ == '__main__':
    main()
