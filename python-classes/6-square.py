#!/usr/bin/python3
"""Module for class Square"""


class Square:
    """Defines a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """This is _init_ function"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is getter for Size property"""
        return self.__size

    @property
    def position (self):
        """This is getter for Position property"""
        return self.__position

    @size.setter
    def size(self, value):
        """This is setter to use: size = x and check the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """This is setter to use: position = x and check the value"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int) or not isinstance(value[1], int)
        or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value          

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prits square with #"""
        if self.size == 0:
            print('')
        else:
            for _ in range(self.position[1]):
              print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
