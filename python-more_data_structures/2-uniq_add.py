#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    new_list = [my_list[0]]
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return sum(new_list)
