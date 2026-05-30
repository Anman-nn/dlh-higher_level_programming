#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
