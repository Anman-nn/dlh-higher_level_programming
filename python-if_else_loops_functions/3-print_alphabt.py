#!/usr/bin/python3
mystr = ""
for i in range(97, 123):
    if i == 113 or i == 101:
        continue
    mystr = mystr + chr(i)
print("{}".format(mystr), end="")
