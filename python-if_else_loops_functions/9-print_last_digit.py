#!/usr/bin/python3
def print_last_digit(number):
    s = str(number)
    lastnum = s[len(s)-1]
    lastnum = int(lastnum)
    print(lastnum, end="")
    return(lastnum)
