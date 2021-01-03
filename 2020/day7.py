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

def open_file(file_name):
    '''
    Get lines from file and create list with them
    '''
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line.strip('.\n'))

    return lines


def data_to_bags(lines):
    '''
    Split lines.
    Pattern: Bag "contain" number_bag bag_name, number_bag bag_name, ...
    '''
    bags_types = []
    bags_dic = dict()
    for line in lines:
        bag, contains = line.split('contain')
        bag = " ".join(bag.split(" ")[:2])
        contains = contains.split(',')

        contains = [cn.strip() for cn in contains] #Delete spaces after and befor

        #Cut last word "bags"
        contains = [" ".join(cont.split(' ')[:-1]) for cont in contains]
        contains = {" ".join(cont.split(' ')[1:]) : cont.split(' ')[0] for cont in contains}

        if bag not in bags_types:
            bags_types.append(bag)
        if bags_dic.get(bag):
            bags_dic.update(bags_dic[bag])
        bags_dic[bag] = contains

    return bags_dic, bags_types

def check_bag(bags, the_bag, current_bag):
    if current_bag == the_bag:
        return 1
    if bags.get(current_bag) is None:
        return 0
    else:
        counts = []
        for k, v in bags[current_bag].items():
            counts.append(check_bag(bags, the_bag, k))
        return max(counts)

def count_bags(bags, current_bag):
    '''
    '''
    for k, v in bags.items():
        if current_bag == " " or bags.get(current_bag) is None :
            return 0

        n = len(bags[current_bag])
        nn = []
        for k in bags[current_bag]:
            nn.append(count_bags(bags, k))
        return sum(nn) + n



def main():
    data = open_file('data/day7_puzzle_input.txt')
    bags_dic, bags = data_to_bags(data)
    result = 0
    my_bag = "shiny gold"
    for k, v in bags_dic.items():
        if k != my_bag:
            result += check_bag(bags_dic, my_bag, k)

    print(result)

    result = 0
    bags_contains = {}

    for k, v in bags_dic.items():
        bags_contains[k] = []
        try:
            for kk, vv in v.items():

                bags_contains[k]+=[kk]*int(vv)
        except:
            pass

    print (count_bags(bags_contains, my_bag))

if __name__ == '__main__':
    main()

####################################################
###################  Example  ######################
####################################################
##
##with open("data/day7_puzzle_input.txt", "r") as fp:
##    lines = fp.readlines()
##    lines=[line.rstrip() for line in lines]
##
### to make a dictionary of bags
##bag_types = []
##all_bags = {}
##for line in lines:
##    mbag = " ".join(line.split(" ")[:2])
##    contains = line[line.index("contain ")+8:-1]
##    each_contain = contains.split(",")
##    each_contain = [cnt.lstrip() for cnt in each_contain]
##    each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
##    print(each_contain)
##    each_contain = {" ".join(cont.split(" ")[1:]):cont.split(" ")[0] for cont in each_contain}
##    print(each_contain)
##    if mbag not in bag_types:
##        bag_types.append(mbag)
##        print('type', bag_types)
##    if all_bags.get(mbag):
##        each_contain.update(all_bags[mbag])
##        print('all_bags', bag_types)
##    all_bags[mbag] = each_contain
##    print('all_bags2', bag_types)
##
##def check_bag(bags, my_bag, current_bag):
##    if current_bag==my_bag:
##        return 1
##    if bags.get(current_bag) is None:
##        return 0
##    else:
##        counts = []
##        for k, v in bags[current_bag].items():
##            counts.append(check_bag(bags, my_bag, k))
##        return max(counts)
##
##found_bags = 0
####my_bag = "shiny gold"
####for k, v in all_bags.items():
####    if k != my_bag:
####        found_bags+=check_bag(all_bags, my_bag, k)
####print(f"{found_bags} bags can contain {my_bag} bag.")
##
##my_bag = "shiny gold"
##bags_contains = {}
##test_bags=all_bags
##for k, v in test_bags.items():
##    bags_contains[k] = []
##    try:
##        for kk, vv in v.items():
##
##            bags_contains[k]+=[kk]*int(vv)
##    except:
##        pass
##c=0
##
##def count_bags(current_bag):
##    if current_bag==" " or bags_contains.get(current_bag) is None:
##        return 0
##
##    #print("key:", current_bag)
##    cnt = len(bags_contains[current_bag])
##    cnts = []
##    for k in bags_contains[current_bag]:
##        cnts.append(count_bags(k))
##    return sum(cnts)+cnt
##
##print(f"{my_bag} bag can hold {count_bags('shiny gold')} bags")