#!/usr/bin/python3
import sys
from pathlib import Path

"""Module providing a utility to manage JSON item lists.

This script checks if 'add_item.json' exists, loads existing data
or initializes empty list, appends command line argument and
saves updated content back."""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_file = Path("add_item.json")


if my_file.is_file():
    """Load existing items into a new list variable.

    Reads current JSON file contents into an item list
    for further processing steps below in this conditional
    block execution flow path only."""

    item: list = []
    item.append(load_from_json_file("add_item.json"))
    item.append(sys.argv[1])
    save_to_json_file(item, "add_item.json")


else:
    """Initialize new single-item list from
    command line argument.

    When file does not exist yet it creates a simple list
    containing only first positional argument passed to
    script execution directly here."""

    item = sys.argv[1]
    save_to_json_file(item, "add_item.json")
