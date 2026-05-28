#!/usr/bin/python3
"""Module: learning input - output"""


def write_file(filename="", text=""):
    """Function write file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
