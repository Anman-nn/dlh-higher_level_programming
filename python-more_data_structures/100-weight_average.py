#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sumtup = 0
    denom = 0
    for tup in my_list:
        k, v = tup[0], tup[1]
        sumtup += k*v
        denom += v
    return sumtup/denom
