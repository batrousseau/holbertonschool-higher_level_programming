#!/usr/bin/python3
"""Module providing a utility to manage JSON item lists.

This script checks if 'add_item.json' exists, loads existing data
or initializes empty list, appends command line argument and
saves updated content back."""

import sys
from pathlib import Path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_file = Path("add_item.json")

if my_file.is_file():

    item = load_from_json_file("add_item.json")
    item.extend(sys.argv[1:])
    save_to_json_file(item, "add_item.json")

else:

    item = sys.argv[1:]
    save_to_json_file(item, "add_item.json")
