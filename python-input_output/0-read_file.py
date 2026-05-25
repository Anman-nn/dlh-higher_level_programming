#!/usr/bin/python3
"""Module: learning input - output"""
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print (read_data)
