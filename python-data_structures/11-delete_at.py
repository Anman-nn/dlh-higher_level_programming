#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """deletes the item at a specific position in a list"""
    return my_list[:idx] + my_list[idx+1:]
