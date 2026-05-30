#!/usr/bin/python3
"""Module: learning input - output"""


def load_from_json_file(filename):
    """Function to_json_string"""
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
