#!/usr/bin/python3
"""Module: learning input - output"""


def read_file(filename=""):
    """Function reads the file and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
