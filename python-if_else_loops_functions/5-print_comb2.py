#!/usr/bin/python3
mystr = ""
for i in range(99):
    if i < 10:
        i = "0" + str(i)
    print("{}, ".format(i), end="")
print("99")
