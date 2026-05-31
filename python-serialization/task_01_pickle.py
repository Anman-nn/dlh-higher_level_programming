#!/usr/bin/python3
"""
a basic serialization module that adds
the functionality to serialize a Python
dictionary to a JSON file and deserialize
the JSON file to recreate the Python Dictionary
"""

import pickle


class CustomObject:
    """This is a class CustomObject"""

    def __init__(self, name="", age=0, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")
    
    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod 
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
