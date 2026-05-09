#!/usr/bin/python3
def no_c(my_string):
    res_string = []
    for s in my_string:
        if s == "c" or s == "C":
            continue
        else:
            res_string.append(s)
    return "".join(res_string)
