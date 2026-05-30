#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # checking for NULL value in a then in B
    if not tuple_a and not tuple_b:
        empty_tuple: tuple = (0, 0)
        return (empty_tuple)
    # checking for minimum lenght of each tuple
    a_clean: tuple = (tuple_a + (0, 0))[:2]
    b_clean: tuple = (tuple_b + (0, 0))[:2]
    tuple_c: tuple = ((a_clean[0] + b_clean[0]), (a_clean[1]) + b_clean[1])
    return (tuple_c)
