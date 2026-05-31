#!/usr/bin/python3

def uniq_add(my_list=[]):

    result: int = 0
    if not my_list:
        return (result)
    only_one = set(my_list)
    clean_list: list = list(only_one)
    for j in range(len(clean_list)):
        result = result + clean_list[j]
    return (result)
