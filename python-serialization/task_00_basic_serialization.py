#!/usr/bin/python3
"""
a basic serialization module that adds
the functionality to serialize a Python
dictionary to a JSON file and deserialize
the JSON file to recreate the Python Dictionary
"""



def serialize_and_save_to_file(data, filename):
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))

def load_and_deserialize(filename):
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
