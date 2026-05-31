#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    empty_dict: dict = {}
    if not a_dictionary:
        return (empty_dict)
    for j, k in (a_dictionary.items()):
        empty_dict[j] = k * 2
    return (empty_dict)
