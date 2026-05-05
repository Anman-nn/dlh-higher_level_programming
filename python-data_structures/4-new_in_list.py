#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_new_list = my_list.copy()
    if idx < 0 or (idx+1) > len(my_list):
        return my_new_list
    else:
        my_new_list[idx] = element
        return my_new_list
