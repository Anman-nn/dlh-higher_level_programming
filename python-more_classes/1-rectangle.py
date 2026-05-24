#!/usr/bin/python3
"""Module: learning more classes, create rectangles"""


class Rectangle:
    """
    Class - Rectangle
    Defines a Rectangle class
    """
    def __init__(self, width=0, heigh=0):
        self.width = width
        self.heigh = heigh
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    
    @property
    def heigh(self):
        return self.__heigh
    
    @heigh.setter
    def heigh(self, value):
        if not isinstance(value, int):
            raise TypeError('heigh must be an integer')
        if value < 0:
            raise ValueError('heigh must be >= 0')
        self.__heigh = value
