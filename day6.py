

def main():
    orbits = tsk.task_list()
    orbits_copy = orbits[:]
    com = Star('COM', None)
    add_child_to_star(com, orbits)
    print('==========1==========')
    print(count_all_orbits(com),'\n')

    print('==========2==========')

    result= []
    path_to_you = path_to('YOU', orbits_copy)
    path_to_san =path_to('SAN', orbits_copy)

    print(set(path_to_you) ^ set(path_to_san))

if __name__ == '__main__':
    main()
