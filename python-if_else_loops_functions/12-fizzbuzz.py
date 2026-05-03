#!/usr/bin/python3
def fizzbuzz():
    for n in range (1, 101):
        output = n
        if n % 15 == 0:
            output = "FizzBuzz"
        elif n % 3 == 0:
            output = "Fizz"
        elif n % 5 == 0:
            output = "Buzz"
        print(output, end=" ")
