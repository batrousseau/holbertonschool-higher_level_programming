#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if not set_1:
        return (set_2)
    if not set_2:
        return (set_1)
    only_set = set(set_1 ^ set_2)
    return (only_set)
