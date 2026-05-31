#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return ("")
    a_dictionary = sorted(a_dictionary.items())
    sort_dir = dict(a_dictionary)
    for i, j in sort_dir.items():
        print(f"{i}: {j}")
