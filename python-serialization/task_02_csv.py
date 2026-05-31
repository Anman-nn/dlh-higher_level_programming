#!/usr/bin/python3
"""
Converting CSV Data to JSON Format
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    res = []
    try:
        with open(csv_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                res.append(row)
        with open('data.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(res))
        return True   
    except Exception:
        return False
