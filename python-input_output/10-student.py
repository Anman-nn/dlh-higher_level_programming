#!/usr/bin/python3
"""Module for a Class - Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        for a in attrs:
            if not isinstance(a, 'str'):
                return self.__dict__

        res = {}
        for a in attrs:
            res[a] = self.__dict__[a]    
        return res
