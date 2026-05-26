#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        copy_list = my_list.copy()
        del copy_list[idx]
        copy_list.insert(idx, element)
        return (copy_list)
