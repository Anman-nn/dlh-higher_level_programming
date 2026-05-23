#!/usr/bin/python3
"""Module for class Square"""
class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        """This is _init_ function"""
        self.size = size
    @property
    def size(self):
        """This is getter for Size attribute"""
        return self.__size
    @size.setter
    def size(self, value):
        """This is setter to use: size = x"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """returns the current square area"""
        return self.__size ** 2
