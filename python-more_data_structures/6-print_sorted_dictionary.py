#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dict = dict(sorted(a_dictionary.items()))
    for k, v in s_dict.items():
        print("{}: {}".format(k, v))
