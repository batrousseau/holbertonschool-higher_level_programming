#!/usr/bin/python3

def common_elements(set_1, set_2):
    if not set_2 or not set_2:
        return (None)
    set_1 = set_1.intersection(set_2)
    return (set_1)
