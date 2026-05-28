#!/usr/bin/python3
"""Module: learning input - output"""


def append_write(filename="", text=""):
    """Function write file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
