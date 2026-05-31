#!/usr/bin/python3
"""
Converting CSV Data to xml Format
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for k, v in dictionary.items():
        child = ET.SubElement(root, k)
        child.text = str(v)
    ET.ElementTree(root).write(filename)

def deserialize_from_xml(filename):
    """Deserialize XML from a file and return a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
