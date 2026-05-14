#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_str = ""
    n = 0
    m = 0
    while n < x:
        try:
            int(my_list[n])
            new_str += str(my_list[n])
            m += 1
        except:
            pass
        n += 1
    try:
        print("{:d}".format(int(new_str)))    
    except:
        return 0
    return m
