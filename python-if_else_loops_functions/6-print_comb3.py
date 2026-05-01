#!/usr/bin/python3
mystr = ""
for i in range(80):
    if i < 10:
        i = "0" + str(i)
    s = str(i)
    if s[1] <= s[0]:
        continue
    print("{}, ".format(s), end="")
print("89")
