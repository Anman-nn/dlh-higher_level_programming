#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new_str = ""
    n = 0
    while n < x:
        try:
            int(my_list[n])
            new_str += str(my_list[n])
        except:
            break
        n += 1
    try:
        print(int(new_str))    
    except:
        return 0
    return n
