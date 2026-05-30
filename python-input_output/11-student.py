#!/usr/bin/python3
"""Module for a Class - Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if not isinstance(attrs, list):
            return self.__dict__

        for a in attrs:
            if not isinstance(a, str):
                return self.__dict__

        res = {}
        for a in attrs:
            try:
                res[a] = self.__dict__[a]
            except KeyError:
                continue
        return res

    def reload_from_json(self, json):
        data = json.loads(json)
        for a, b in data.items():
            setattr(self, a, b)
