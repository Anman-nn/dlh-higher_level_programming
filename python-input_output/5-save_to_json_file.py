#!/usr/bin/python3
"""Module: learning input - output"""


def save_to_json_file(my_obj, filename):
    """Function to_json_string"""
    import json
    with open(filename, encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
