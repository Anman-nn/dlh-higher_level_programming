#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for a in str:
        if ord(a) > 122 or ord(a) < 97:
            newstr = newstr + a
        else:
            newstr = newstr + chr(ord(a) - 32)
    return newstr
