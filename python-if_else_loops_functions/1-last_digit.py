#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number%10
if last > 5:
    ending = "and is greater than 5"
elif last == 0:
    ending = "and is 0"
else:
    ending = "and is less than 6 and not 0"
print(f'Last digit of {number} is {last} {ending}')
